import numpy as np
from bvh.skeleton import Skeleton


class Body25(Skeleton):
    def __init__(self):
        self.root_index = 8
        self.joint2index = {
            "nose": 0, "neck": 1, "shoulder_r": 2, "elbow_r": 3, "wrist_r": 4, "shoulder_l": 5,
            "elbow_l": 6, "wrist_l": 7, "hip_m": 8, "hip_r": 9, "knee_r": 10, "ankle_r": 11,
            "hip_l": 12, "knee_l": 13, "ankle_l": 14, "eye_r": 15, "eye_l": 16, "ear_r": 17,
            "ear_l": 18, "big_toe_l": 19, "small_toe_l": 20, "heel_l": 21, "big_toe_r": 22,
            "small_toe_r": 23, "heel_r": 24
        }
        # coord same as the 3d pose, [x, y, x], x's direction is left,
        # y' direction is far away with the camera, z's direction is up.
        self.con2dir = {
            (1, 0): [0, 0, 1],  # neck -> nose
            (1, 2): [-1, 0, 0],  # neck -> shoulder_r
            (2, 3): [-1, 0, 0],  # shoulder_r -> elbow_r
            (3, 4): [-1, 0, 0],  # elbow_r -> wrist_r
            (1, 5): [1, 0, 0],  # neck -> shoulder_l
            (5, 6): [1, 0, 0],
            (6, 7): [1, 0, 0],
            (8, 1): [0, 0, 1],  # hip_m -> neck
            (8, 9): [-1, 0, 0],  # hip_m -> hip_r
            (9, 10): [0, 0, -1],  # hip_r -> knee_r
            (10, 11): [0, 0, -1],  # knee_r -> ankle_r
            (8, 12): [1, 0, 0],
            (12, 13): [0, 0, -1],
            (13, 14): [0, 0, -1],
            (0, 15): [-1, 0, 0],
            (0, 16): [1, 0, 0],
            (15, 17): [0, 1, 0],  # eye_r -> ear_r
            (16, 18): [0, 1, 0],
            (14, 19): [0, -1, 0],
            (19, 20): [1, 0, 0],
            (14, 21): [0, 1, 0],
            (11, 22): [0, -1, 0],
            (22, 23): [-1, 0, 0],
            (11, 24): [0, 1, 0]
        }
        super(Body25, self).__init__(root_index=self.root_index, joint2index=self.joint2index, con2dir=self.con2dir)

    def get_curr_coord(self, joint, pose):
        index = self.joint2index
        joint_idx = self.joint2index[joint]
        if joint == 'hip_m':
            x_dir = pose[index['hip_l']] - pose[index['hip_r']]
            y_dir = None
            z_dir = pose[index['neck']] - pose[joint_idx]
            order = 'xyz'
        elif joint == 'hip_l':
            x_dir = None
            y_dir = pose[index['heel_l']] - pose[joint_idx]
            z_dir = pose[joint_idx] - pose[index['knee_l']]
            order = 'zxy'
        elif joint == 'hip_r':
            x_dir = None
            y_dir = pose[index['heel_r']] - pose[joint_idx]
            z_dir = pose[joint_idx] - pose[index['knee_r']]
            order = 'zxy'
        elif joint == "neck":
            x_dir = pose[index["shoulder_l"]] - pose[index["shoulder_r"]]
            y_dir = None
            z_dir = pose[index["nose"]] - pose[joint_idx]
            order = 'xyz'
        elif joint == "shoulder_l":
            x_dir = pose[index['elbow_l']] - pose[joint_idx]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index['wrist_l']]
            order = 'xyz'
        elif joint == "shoulder_r":
            x_dir = pose[joint_idx] - pose[index['elbow_r']]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index['wrist_r']]
            order = 'xyz'
        elif joint == "elbow_l":
            x_dir = pose[index['wrist_l']] - pose[joint_idx]
            y_dir = None
            z_dir = pose[index['wrist_l']] - pose[index['shoulder_l']]
            order = 'xyz'
        elif joint == "elbow_r":
            x_dir = pose[joint_idx] - pose[index['wrist_r']]
            y_dir = None
            z_dir = pose[index['shoulder_r']] - pose[index['wrist_r']]
            order = 'xyz'
        elif joint == "knee_l":
            x_dir = pose[joint_idx] - pose[index['hip_m']]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index['ankle_l']]
            order = 'zyx'
        elif joint == "knee_r":
            x_dir = pose[index['hip_m']] - pose[joint_idx]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index['ankle_r']]
            order = 'zyx'
        elif joint == "ankle_l":
            x_dir = None
            y_dir = pose[index['heel_l']] - pose[index['big_toe_l']]
            z_dir = pose[index['hip_m']] - pose[index['big_toe_r']]
            order = 'yxz'
        elif joint == "ankle_r":
            x_dir = None
            y_dir = pose[index['heel_r']] - pose[index['big_toe_r']]
            z_dir = pose[index['hip_m']] - pose[index['big_toe_l']]
            order = 'yxz'
        elif joint == "big_toe_l":
            x_dir = pose[index["small_toe_l"]] - pose[joint_idx]
            y_dir = pose[index["ankle_l"]] - pose[joint_idx]
            z_dir = None
            order = "xzy"
        elif joint == "big_toe_r":
            x_dir = pose[joint_idx] - pose[index["small_toe_r"]]
            y_dir = pose[index["ankle_r"]] - pose[joint_idx]
            z_dir = None
            order = "xzy"
        # elif joint == "eye_l":
        #     x_dir = pose[index["ear_l"]] - pose[index["nose"]]
        #     y_dir = pose[joint_idx] - pose[index["ear_l"]]
        #     z_dir = None
        #     order = "yzx"
        # elif joint == "eye_r":
        #     x_dir = pose[index["nose"]] - pose[index["ear_r"]]
        #     y_dir = pose[joint_idx] - pose[index["ear_r"]]
        #     z_dir = None
        #     order = "yzx"
        else:
            x_dir, y_dir, z_dir, order = None, None, None, None

        return x_dir, y_dir, z_dir, order


if __name__ == "__main__":
    with open("opt0.npy", "rb") as f:
        pose3ds = np.load(f)
        pose3ds = pose3ds[:, :, :3]
    print("pose3ds shape:", pose3ds.shape)

    Body25().poses2bvh(pose3ds, output_file="test.bvh")
