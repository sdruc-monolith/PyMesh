#!/usr/bin/env python

"""
Remove exactly degenerated triangles.
"""

import argparse
import pymesh.meshutils as mu
import pymesh.meshio as mio


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--num-iterations", "-n", type=int, default=5, help="max number of iterations"
    )
    parser.add_argument("input_mesh", help="input triangular mesh")
    parser.add_argument("output_mesh", help="output triangular mesh")
    return parser.parse_args()


def main():
    args = parse_args()
    mesh = mio.load_mesh(args.input_mesh)
    mesh, __ = mu.remove_degenerated_triangles(mesh, args.num_iterations)
    mio.save_mesh(args.output_mesh, mesh)


if __name__ == "__main__":
    main()
