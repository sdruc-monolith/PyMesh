from tests.base_case import TestCase
from pymesh.wires.wire_network import WireNetwork

import numpy as np


class WireTestCase(TestCase):
    def setUp(self):
        super(WireTestCase, self).setUp()

    def get_brick5(self):
        vertices = np.array(
            [
                -1.000000,
                -1.000000,
                1.000000,
                -1.000000,
                -1.000000,
                -1.000000,
                1.000000,
                -1.000000,
                -1.000000,
                1.000000,
                -1.000000,
                1.000000,
                -1.000000,
                1.000000,
                1.000000,
                -1.000000,
                1.000000,
                -1.000000,
                1.000000,
                1.000000,
                -1.000000,
                1.000000,
                1.000000,
                1.000000,
                1.000000,
                0.000000,
                0.000000,
                0.000000,
                -1.000000,
                0.000000,
                -1.000000,
                0.000000,
                0.000000,
                0.000000,
                0.000000,
                -1.000000,
                0.000000,
                0.000000,
                1.000000,
                0.000000,
                1.000000,
                0.000000,
                1.500000,
                0.000000,
                0.000000,
                -1.500000,
                0.000000,
                0.000000,
                0.000000,
                1.500000,
                0.000000,
                0.000000,
                -1.500000,
                0.000000,
                0.000000,
                0.000000,
                1.500000,
                0.000000,
                0.000000,
                -1.500000,
            ],
            dtype=float,
        ).reshape((-1, 3))
        edges = (
            np.array(
                [
                    8,
                    9,
                    14,
                    5,
                    2,
                    10,
                    6,
                    14,
                    14,
                    7,
                    12,
                    2,
                    13,
                    1,
                    12,
                    3,
                    7,
                    12,
                    11,
                    1,
                    12,
                    6,
                    10,
                    4,
                    5,
                    13,
                    2,
                    11,
                    10,
                    1,
                    11,
                    5,
                    9,
                    7,
                    6,
                    11,
                    9,
                    4,
                    9,
                    3,
                    13,
                    8,
                    14,
                    8,
                    10,
                    3,
                    13,
                    4,
                    9,
                    15,
                    11,
                    16,
                    14,
                    17,
                    10,
                    18,
                    13,
                    19,
                    12,
                    20,
                ],
                dtype=int,
            ).reshape((-1, 2))
            - 1
        )
        return WireNetwork.create_from_data(vertices, edges)

    def get_star_3D(self):
        vertices = np.array(
            [
                [0, 0, 0],
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 1],
                [1, 1, 1],
                [0, 1, 1],
                [0.5, 0.5, 0.5],
            ],
            dtype=float,
        )
        edges = np.array(
            [
                [0, 8],
                [1, 8],
                [2, 8],
                [3, 8],
                [4, 8],
                [5, 8],
                [6, 8],
                [7, 8],
            ]
        )
        return WireNetwork.create_from_data(vertices, edges)

    def get_star_2D(self):
        vertices = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.5]], dtype=float)
        edges = np.array(
            [
                [0, 4],
                [1, 4],
                [2, 4],
                [3, 4],
            ]
        )
        return WireNetwork.create_from_data(vertices, edges)

    def get_cross_3D(self):
        vertices = np.array(
            [
                [0.5, 0.0, 0.0],
                [-0.5, 0.0, 0.0],
                [0.0, 0.5, 0.0],
                [0.0, -0.5, 0.0],
                [0.0, 0.0, 0.5],
                [0.0, 0.0, -0.5],
                [0.0, 0.0, 0.0],
            ],
            dtype=float,
        )
        edges = np.array(
            [
                [0, 6],
                [1, 6],
                [2, 6],
                [3, 6],
                [4, 6],
                [5, 6],
            ]
        )
        return WireNetwork.create_from_data(vertices, edges)

    def get_pattern1065(self):
        vertices = np.array(
            [
                0.000000,
                0.000000,
                0.000000,
                0.000000,
                0.250000,
                0.000000,
                0.250000,
                0.500000,
                0.250000,
                0.250000,
                0.250000,
                0.250000,
                0.000000,
                0.000000,
                0.250000,
                0.250000,
                0.250000,
                0.500000,
                0.250000,
                0.000000,
                0.000000,
                0.500000,
                0.250000,
                0.250000,
                -0.250000,
                0.500000,
                0.250000,
                -0.250000,
                0.250000,
                0.250000,
                -0.250000,
                0.250000,
                0.500000,
                -0.250000,
                0.000000,
                0.000000,
                -0.500000,
                0.250000,
                0.250000,
                0.000000,
                -0.250000,
                0.000000,
                0.250000,
                -0.500000,
                0.250000,
                0.250000,
                -0.250000,
                0.250000,
                0.250000,
                -0.250000,
                0.500000,
                0.500000,
                -0.250000,
                0.250000,
                -0.250000,
                -0.500000,
                0.250000,
                -0.250000,
                -0.250000,
                0.250000,
                -0.250000,
                -0.250000,
                0.500000,
                -0.500000,
                -0.250000,
                0.250000,
                0.250000,
                0.500000,
                -0.250000,
                0.250000,
                0.250000,
                -0.250000,
                0.000000,
                0.000000,
                -0.250000,
                0.250000,
                0.250000,
                -0.500000,
                0.500000,
                0.250000,
                -0.250000,
                -0.250000,
                0.500000,
                -0.250000,
                -0.250000,
                0.250000,
                -0.250000,
                -0.250000,
                0.250000,
                -0.500000,
                -0.500000,
                0.250000,
                -0.250000,
                0.250000,
                -0.500000,
                -0.250000,
                0.250000,
                -0.250000,
                -0.250000,
                0.250000,
                -0.250000,
                -0.500000,
                0.500000,
                -0.250000,
                -0.250000,
                -0.250000,
                -0.500000,
                -0.250000,
                -0.250000,
                -0.250000,
                -0.250000,
                -0.250000,
                -0.250000,
                -0.500000,
                -0.500000,
                -0.250000,
                -0.250000,
            ],
            dtype=float,
        ).reshape((-1, 3))
        edges = (
            np.array(
                [
                    3,
                    2,
                    3,
                    4,
                    6,
                    4,
                    8,
                    7,
                    8,
                    4,
                    6,
                    5,
                    2,
                    1,
                    9,
                    2,
                    9,
                    10,
                    11,
                    5,
                    11,
                    10,
                    13,
                    12,
                    13,
                    10,
                    5,
                    1,
                    15,
                    14,
                    15,
                    16,
                    17,
                    5,
                    17,
                    16,
                    18,
                    7,
                    18,
                    16,
                    7,
                    1,
                    19,
                    20,
                    21,
                    5,
                    21,
                    20,
                    22,
                    12,
                    22,
                    20,
                    19,
                    14,
                    27,
                    7,
                    27,
                    24,
                    26,
                    25,
                    26,
                    24,
                    23,
                    2,
                    23,
                    24,
                    28,
                    29,
                    30,
                    25,
                    31,
                    29,
                    12,
                    1,
                    31,
                    12,
                    25,
                    1,
                    30,
                    29,
                    28,
                    2,
                    32,
                    14,
                    32,
                    33,
                    34,
                    25,
                    35,
                    7,
                    35,
                    33,
                    34,
                    33,
                    38,
                    25,
                    39,
                    37,
                    39,
                    12,
                    38,
                    37,
                    14,
                    1,
                    36,
                    14,
                    36,
                    37,
                ]
            ).reshape((-1, 2))
            - 1
        )
        return WireNetwork.create_from_data(vertices, edges)

    def load_wires(self, wire_file):
        wire_network = WireNetwork()
        wire_network.load_from_file(wire_file)
        return wire_network

    def save_wires(self, wire_network, wire_file):
        wire_network.write_to_file(wire_file)