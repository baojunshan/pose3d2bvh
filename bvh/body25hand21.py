from bvh.skeleton import Skeleton


class Body25Hand21(Skeleton):
    def __init__(self):
        self.root_index = 8
        self.joint2index = {
            "nose": 0, "neck": 1, "shoulder_r": 2, "elbow_r": 3, "wrist_r": 4, "shoulder_l": 5,
            "elbow_l": 6, "wrist_l": 7, "hip_m": 8, "hip_r": 9, "knee_r": 10, "ankle_r": 11,
            "hip_l": 12, "knee_l": 13, "ankle_l": 14, "eye_r": 15, "eye_l": 16, "ear_r": 17,
            "ear_l": 18, "big_toe_l": 19, "small_toe_l": 20, "heel_l": 21, "big_toe_r": 22,
            "small_toe_r": 23, "heel_r": 24,

            "wristh_l": 25, "thumb_cmc_l": 26, "thumb_mcp_l": 27, "thumb_ip_l": 28, "thumb_tip_l": 29,
            "index_finger_mcp_l": 30, "index_finger_pip_l": 31, "index_finger_dip_l": 32, "index_finger_tip_l": 33,
            "middle_finger_mcp_l": 34, "middle_finger_pip_l": 35, "middle_finger_dip_l": 36, "middle_finger_tip_l": 37,
            "ring_finger_mcp_l": 38, "ring_finger_pip_l": 39, "ring_finger_dip_l": 40, "ring_finger_tip_l": 41,
            "pinky_finger_mcp_l": 42, "pinky_finger_pip_l": 43, "pinky_finger_dip_l": 44, "pinky_finger_tip_l": 45,

            "wristh_r": 46, "thumb_cmc_r": 47, "thumb_mcp_r": 48, "thumb_ip_r": 49, "thumb_tip_r": 50,
            "index_finger_mcp_r": 51, "index_finger_pip_r": 52, "index_finger_dip_r": 53, "index_finger_tip_r": 54,
            "middle_finger_mcp_r": 55, "middle_finger_pip_r": 56, "middle_finger_dip_r": 57, "middle_finger_tip_r": 58,
            "ring_finger_mcp_r": 59, "ring_finger_pip_r": 60, "ring_finger_dip_r": 61, "ring_finger_tip_r": 62,
            "pinky_finger_mcp_r": 63, "pinky_finger_pip_r": 64, "pinky_finger_dip_r": 65, "pinky_finger_tip_r": 66
        }
        # coord same as the 3d pose, [x, y, x], x's direction is right,
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
            (11, 24): [0, 1, 0],

            (7, 26): [1, 0, 1],  # w -> thumb1
            (26, 27): [1, 0, 0],  # thumb1 -> thumb2
            (27, 28): [1, 0, 0],
            (28, 29): [1, 0, 0],
            (7, 30): [3, 0, 1],  # w->index_finger
            (30, 31): [1, 0, 0],  # index_finger 1>2
            (31, 32): [1, 0, 0],
            (32, 33): [1, 0, 0],
            (7, 34): [1, 0, 0],  # w -> middle_finger
            (34, 35): [1, 0, 0],  # middle_finger 1>2
            (35, 36): [1, 0, 0],
            (36, 37): [1, 0, 0],
            (7, 38): [3, 0, -1],  # w -> ring_finger
            (38, 39): [1, 0, 0],  # ring_finger 1> 2
            (39, 40): [1, 0, 0],
            (40, 41): [1, 0, 0],
            (7, 42): [2, 0, -1],  # w -> pinky_finger
            (42, 43): [1, 0, 0],
            (43, 44): [1, 0, 0],
            (44, 45): [1, 0, 0],

            (4, 47): [-1, 0, 1],  # w -> thumb1
            (47, 48): [-1, 0, 0],  # thumb1 -> thumb2
            (48, 49): [-1, 0, 0],
            (49, 50): [-1, 0, 0],
            (4, 51): [-3, 0, 1],  # w->index_finger
            (51, 52): [-1, 0, 0],  # index_finger 1>2
            (52, 53): [-1, 0, 0],
            (53, 54): [-1, 0, 0],
            (4, 55): [-1, 0, 0],  # w -> middle_finger
            (55, 56): [-1, 0, 0],  # middle_finger 1>2
            (56, 57): [-1, 0, 0],
            (57, 58): [-1, 0, 0],
            (4, 59): [-3, 0, -1],  # w -> ring_finger
            (59, 60): [-1, 0, 0],  # ring_finger 1> 2
            (60, 61): [-1, 0, 0],
            (61, 62): [-1, 0, 0],
            (4, 63): [-2, 0, -1],  # w -> pinky_finger
            (63, 64): [-1, 0, 0],
            (64, 65): [-1, 0, 0],
            (65, 66): [-1, 0, 0],
        }
        super(Body25Hand21, self).__init__(root_index=self.root_index, joint2index=self.joint2index,
                                           con2dir=self.con2dir)

    def get_curr_coord(self, joint, pose):
        index = self.joint2index
        joint_idx = self.joint2index[joint]
        if joint == 'hip_m':
            x_dir = pose[index['hip_l']] - pose[index['hip_r']]
            y_dir = None
            z_dir = pose[index['neck']] - pose[joint_idx]
            order = 'xyz'
        elif joint.startswith("hip"):
            suffix = joint[-1]
            x_dir = None
            y_dir = pose[index[f'heel_{suffix}']] - pose[joint_idx]
            z_dir = pose[joint_idx] - pose[index[f'knee_{suffix}']]
            order = 'zxy'
        elif joint == "neck":
            x_dir = pose[index["shoulder_l"]] - pose[index["shoulder_r"]]
            y_dir = None
            z_dir = pose[index["nose"]] - pose[joint_idx]
            order = 'xyz'
        elif joint.startswith("shoulder"):
            suffix = joint[-1]
            x_dir = pose[index['elbow_l']] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f'elbow_{suffix}']]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index[f'wrist_{suffix}']]
            order = 'xyz'
        elif joint.startswith("elbow"):
            suffix = joint[-1]
            x_dir = pose[index[f'wrist_{suffix}']] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f'wrist_{suffix}']]
            y_dir = None
            z_dir = pose[index[f'wrist_{suffix}']] - pose[index[f'shoulder_{suffix}']]
            order = 'xyz'

        elif joint.startswith("knee"):
            suffix = joint[-1]
            x_dir = pose[joint_idx] - pose[index['hip_m']] if suffix == "l" else \
                pose[index['hip_m']] - pose[joint_idx]
            y_dir = None
            z_dir = pose[joint_idx] - pose[index[f'ankle_{suffix}']]
            order = 'zyx'
        elif joint.startswith("ankle"):
            suffix = joint[-1]
            x_dir = None
            y_dir = pose[index[f'heel_{suffix}']] - pose[index[f'big_toe_{suffix}']]
            z_dir = pose[index['hip_m']] - pose[index[f'big_toe_{suffix}']]
            order = 'yxz'
        # elif joint.startswith("eye"):
        #     suffix = joint[-1]
        #     x_dir = pose[index[f"ear_{suffix}"]] - pose[index["nose"]] if suffix == "l" else \
        #         pose[index["nose"]] - pose[index[f"ear_{suffix}"]]
        #     y_dir = pose[joint_idx] - pose[index[f"ear_{suffix}"]]
        #     z_dir = None
        #     order = "yzx"
        elif joint.startswith("wrist"):
            suffix = joint[-1:]
            x_dir = pose[index[f"middle_finger_mcp_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"middle_finger_mcp_{suffix}"]]
            y_dir = None
            z_dir = pose[index[f"index_finger_mcp_{suffix}"]] - pose[index[f"pinky_finger_mcp_{suffix}"]]
            order = "xyz"

        elif joint.startswith("thumb_cmc"):
            suffix = joint[-1:]
            x_dir = pose[index[f"thumb_mcp_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"thumb_mcp_{suffix}"]]
            y_dir = None
            z_dir = pose[index[f"thumb_mcp_{suffix}"]] - pose[index[f"wrist_{suffix}"]]
            order = "xyz"
        elif joint.startswith("thumb_mcp"):
            suffix = joint[-1:]
            x_dir = pose[index[f"thumb_ip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"thumb_ip_{suffix}"]]
            y_dir = None
            z_dir = pose[index[f"thumb_ip_{suffix}"]] - pose[index[f"thumb_cmc_{suffix}"]]
            order = "xyz"
        elif joint.startswith("thumb_ip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"thumb_tip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"thumb_tip_{suffix}"]]
            y_dir = None
            z_dir = pose[index[f"thumb_tip_{suffix}"]] - pose[index[f"thumb_mcp_{suffix}"]]
            order = "xyz"

        elif joint.startswith("index_finger_mcp"):
            suffix = joint[-1:]
            x_dir = pose[index[f"index_finger_pip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"index_finger_pip_{suffix}"]]
            y_dir = pose[index[f"index_finger_pip_{suffix}"]] - pose[index[f"wrist_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("index_finger_pip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"index_finger_dip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"index_finger_dip_{suffix}"]]
            y_dir = pose[index[f"index_finger_dip_{suffix}"]] - pose[index[f"index_finger_mcp_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("index_finger_dip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"index_finger_tip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"index_finger_tip_{suffix}"]]
            y_dir = pose[index[f"index_finger_tip_{suffix}"]] - pose[index[f"index_finger_pip_{suffix}"]]
            z_dir = None
            order = "xzy"

        elif joint.startswith("middle_finger_mcp"):
            suffix = joint[-1:]
            x_dir = pose[index[f"middle_finger_pip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"middle_finger_pip_{suffix}"]]
            y_dir = pose[index[f"middle_finger_pip_{suffix}"]] - pose[index[f"wrist_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("middle_finger_pip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"middle_finger_dip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"middle_finger_dip_{suffix}"]]
            y_dir = pose[index[f"middle_finger_dip_{suffix}"]] - pose[index[f"middle_finger_mcp_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("middle_finger_dip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"middle_finger_tip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"middle_finger_tip_{suffix}"]]
            y_dir = pose[index[f"middle_finger_tip_{suffix}"]] - pose[index[f"middle_finger_pip_{suffix}"]]
            z_dir = None
            order = "xzy"

        elif joint.startswith("ring_finger_mcp"):
            suffix = joint[-1:]
            x_dir = pose[index[f"ring_finger_pip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"ring_finger_pip_{suffix}"]]
            y_dir = pose[index[f"ring_finger_pip_{suffix}"]] - pose[index[f"wrist_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("ring_finger_pip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"ring_finger_dip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"ring_finger_dip_{suffix}"]]
            y_dir = pose[index[f"ring_finger_dip_{suffix}"]] - pose[index[f"ring_finger_mcp_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("ring_finger_dip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"ring_finger_tip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"ring_finger_tip_{suffix}"]]
            y_dir = pose[index[f"ring_finger_tip_{suffix}"]] - pose[index[f"ring_finger_pip_{suffix}"]]
            z_dir = None
            order = "xzy"

        elif joint.startswith("pinky_finger_mcp"):
            suffix = joint[-1:]
            x_dir = pose[index[f"pinky_finger_pip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"pinky_finger_pip_{suffix}"]]
            y_dir = pose[index[f"pinky_finger_pip_{suffix}"]] - pose[index[f"wrist_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("pinky_finger_pip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"pinky_finger_dip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"pinky_finger_dip_{suffix}"]]
            y_dir = pose[index[f"pinky_finger_dip_{suffix}"]] - pose[index[f"pinky_finger_mcp_{suffix}"]]
            z_dir = None
            order = "xzy"
        elif joint.startswith("pinky_finger_dip"):
            suffix = joint[-1:]
            x_dir = pose[index[f"pinky_finger_tip_{suffix}"]] - pose[joint_idx] if suffix == "l" else \
                pose[joint_idx] - pose[index[f"pinky_finger_tip_{suffix}"]]
            y_dir = pose[index[f"pinky_finger_tip_{suffix}"]] - pose[index[f"pinky_finger_pip_{suffix}"]]
            z_dir = None
            order = "xzy"



        else:
            x_dir, y_dir, z_dir, order = None, None, None, None

        return x_dir, y_dir, z_dir, order