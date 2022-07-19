import numpy as np
from typing import Union
from bvh import bvh_helper
from bvh import math3d


class Skeleton:
    def __init__(self, root_index, joint2index, con2dir):
        self.root_index = root_index
        self.joint2index = joint2index
        self.con2dir = con2dir

        self.index2joint = {v: k for k, v in self.joint2index.items()}

        self.children = dict()
        for p, c in self.con2dir.keys():
            self.children[p] = self.children.get(p, list()) + [c]

        self.parent = {c: p for p, c in self.con2dir.keys()}
        self.parent.update({self.root_index: None})

    def _get_bone_length(self, pose3ds: np.array):
        if pose3ds.ndim == 2:
            pose3ds = pose3ds[None, ...]
        assert pose3ds.ndim == 3, f"`pose3ds' shape should be [n_frame, n_joint, 3 or 4]`"

        bone_length = dict()
        for p, c in self.con2dir.keys():
            filter_ = True
            if pose3ds.shape[-1] == 4:
                filter_ = np.where((pose3ds[:, p, 3] > 0.1) & (pose3ds[:, c, 3] > 0.1))[0]
            bone_length[c] = np.linalg.norm(pose3ds[filter_, p, :3] - pose3ds[filter_, c, :3], axis=1).mean()
        for k in bone_length.keys():
            suffix = self.index2joint[k][-2:]
            stem = self.index2joint[k][:-2]
            if suffix in ("_l" or "_r"):
                avg_len = (bone_length[self.joint2index[stem + "_l"]] + bone_length[self.joint2index[stem + "_r"]]) / 2
                bone_length[self.joint2index[stem + "_l"]] = avg_len
                bone_length[self.joint2index[stem + "_r"]] = avg_len
        return bone_length

    def _get_init_offset(self, pose3ds: np.array):
        bone_length = self._get_bone_length(pose3ds)
        init_offset = dict()
        for (p, c), d in self.con2dir.items():
            d = np.array(d) / max(np.linalg.norm(d), 1e-12)
            init_offset[c] = d * bone_length[c]
        init_offset[self.root_index] = pose3ds[0, self.root_index, :3]  # FIXME
        return init_offset

    def get_bvh_header(self, pose3ds: np.array):
        init_offset = self._get_init_offset(pose3ds)

        nodes = dict()
        for idx, name in self.index2joint.items():
            is_root = idx == self.root_index
            is_end_site = len(self.children.get(idx, list())) == 0
            nodes[name] = bvh_helper.BvhNode(
                name=name,
                offset=init_offset.get(idx, 0.0),
                rotation_order='zxy' if not is_end_site else '',
                is_root=is_root,
                is_end_site=is_end_site,
            )
        for pid, cids in self.children.items():
            nodes[self.index2joint[pid]].children = [nodes[self.index2joint[cid]] for cid in cids]
            for cid in cids:
                nodes[self.index2joint[cid]].parent = nodes[self.index2joint[pid]]

        header = bvh_helper.BvhHeader(root=nodes[self.index2joint[self.root_index]], nodes=nodes)
        return header

    def get_curr_coord(self, joint, pose):
        raise ImportError

    def pose2euler(self, pose, header):
        channel = list()
        quats = dict()
        eulers = dict()
        stack = [header.root]
        while stack:
            node = stack.pop()
            joint = node.name

            if node.is_root:
                channel.extend(pose[self.joint2index[joint]])

            x_dir, y_dir, z_dir, order = self.get_curr_coord(joint=joint, pose=pose)

            if order:
                dcm = math3d.dcm_from_axis(x_dir, y_dir, z_dir, order)
                quats[joint] = math3d.dcm2quat(dcm)
            else:
                quats[joint] = quats[self.index2joint[self.parent[self.joint2index[joint]]]].copy()

            local_quat = quats[joint].copy()
            if node.parent:
                local_quat = math3d.quat_divide(
                    q=quats[joint], r=quats[node.parent.name]
                )

            euler = math3d.quat2euler(
                q=local_quat, order=node.rotation_order
            )
            euler = np.rad2deg(euler)
            eulers[joint] = euler
            channel.extend(euler)

            for child in node.children[::-1]:
                if not child.is_end_site:
                    stack.append(child)

        return channel

    def poses2bvh(self,
                  pose3ds: np.array,
                  header: Union[None, bvh_helper.BvhHeader] = None,
                  output_file: Union[None, str] = None):
        if not header:
            header = self.get_bvh_header(pose3ds)

        channels = []
        channels.append([0] * (len(self.index2joint.keys()) + 1) * 3)
        for frame, pose in enumerate(pose3ds):
            channel = self.pose2euler(pose[:, :3], header)
            channels.append(channel)

        if output_file:
            bvh_helper.write_bvh(output_file, header, channels)

        return channels, header

