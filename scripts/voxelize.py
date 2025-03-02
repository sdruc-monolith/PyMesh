#!/usr/bin/env python

""" Compute voxelization of an input mesh.
"""

import argparse
from pymesh.voxel_grid import VoxelGrid
import pymesh.meshio as mio


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cell-size", default=1.0, type=float, help="size of each voxel"
    )
    parser.add_argument(
        "--erode", help="erode N layers of voxel", default=0, type=int, metavar="N"
    )
    parser.add_argument(
        "--dilate", help="dilate N layers of voxel", default=0, type=int, metavar="N"
    )
    parser.add_argument("input_mesh")
    parser.add_argument("output_mesh")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    mesh = mio.load_mesh(args.input_mesh)
    grid = VoxelGrid(args.cell_size, mesh.dim)
    grid.insert_mesh(mesh)
    grid.create_grid()
    grid.dilate(args.dilate)
    grid.erode(args.erode)
    out_mesh = grid.mesh
    mio.save_mesh(args.output_mesh, out_mesh)


if __name__ == "__main__":
    main()
