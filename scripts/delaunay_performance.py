#!/usr/bin/env python

import timeit

N = 5
repeats = 10000

r = timeit.timeit(
    "triangulate_beta(pts, engine='igl_lexicographic')",
    setup="import numpy.random; from pymesh.traingulate import triangulate_beta; pts = numpy.random.rand({}, 2)".format(
        N
    ),
    number=repeats,
)
print("igl lexicographic: {}".format(r / repeats))

r = timeit.timeit(
    "triangulate_beta(pts, engine='igl_delaunay')",
    setup="import numpy.random; from pymesh.traingulate import triangulate_beta; pts = numpy.random.rand({}, 2)".format(
        N
    ),
    number=repeats,
)
print("igl delaunay:      {}".format(r / repeats))

r = timeit.timeit(
    "triangulate_beta(pts, engine='shewchuk_triangle')",
    setup="import numpy.random; from pymesh.traingulate import triangulate_beta; pts = numpy.random.rand({}, 2)".format(
        N
    ),
    number=repeats,
)
print("shewchuk:          {}".format(r / repeats))

r = timeit.timeit(
    "triangulate_beta(pts, engine='cgal_delaunay')",
    setup="import numpy.random; from pymesh.traingulate import triangulate_beta; pts = numpy.random.rand({}, 2)".format(
        N
    ),
    number=repeats,
)
print("cgal:              {}".format(r / repeats))

r = timeit.timeit(
    "triangulate_beta(pts, engine='geogram_delaunay')",
    setup="import numpy.random; from pymesh.traingulate import triangulate_beta; pts = numpy.random.rand({}, 2)".format(
        N
    ),
    number=repeats,
)
print("geogram:           {}".format(r / repeats))
