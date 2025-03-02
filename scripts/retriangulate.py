#!/usr/bin/env python

"""
Retriangulate 2D and 3D planar meshes.
"""

import argparse
import pymesh.meshio as mio
from pymesh.triangle import triangle


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-area", "-a", required=True, help="Max triangle area", type=float
    )
    parser.add_argument("--no-split-boundary", action="store_true")
    parser.add_argument("--no-steiner-points", action="store_true")
    parser.add_argument("input_mesh", help="Input mesh")
    parser.add_argument("output_mesh", help="Output mesh")
    return parser.parse_args()


def main():
    args = parse_args()
    mesh = mio.load_mesh(args.input_mesh)
    engine = triangle()
    engine.points = mesh.vertices
    engine.triangles = mesh.faces
    engine.max_area = args.max_area
    engine.split_boundary = not args.no_split_boundary
    if args.no_steiner_points:
        engine.max_num_steiner_points = 0

    engine.run()
    mesh = engine.mesh
    mio.save_mesh(args.output_mesh, mesh)


if __name__ == "__main__":
    main()
