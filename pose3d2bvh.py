import argparse
import numpy as np

from bvh.body25hand21 import Body25Hand21
from bvh.body25 import Body25


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_path", default='data/pose.npy', type=str, help="input pose3d file")
parser.add_argument("-o", "--output_path", default='0.bvh', type=str, help="the output path of the bvh results")
parser.add_argument("-s", "--skeleton", default="body25hand21", help="skeleton type [body25hand21, body25]")
args = parser.parse_args()


if __name__ == "__main__":
    pose3d = np.load(args.input_path)

    if args.skeleton == "body25hand21":
        Body25Hand21().poses2bvh(pose3d[:, :25 + 21 + 21, ...], output_file=args.output_path)
    elif args.skeleton == "body25":
        Body25().poses2bvh(pose3d[:, :25, ...], output_file=args.output_path)
    else:
        raise ValueError(f"skeleton now just has two type [body25hand21, body25], but get input {args.skeleton}.")
