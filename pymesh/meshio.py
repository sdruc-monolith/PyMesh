import numpy as np
import os.path

from .mesh import Mesh
import PyMesh

from .save_svg import save_svg


def load_mesh(filename, extension_hint=None, drop_zero_dim=False):
    """Load mesh from a file.

    Args:
        filename: Input filename.  File format is auto detected based on
            extension.
        drop_zero_dim (bool): If true, convert flat 3D mesh into 2D mesh.

    Returns:
        A :py:class:`Mesh` object representing the loaded mesh.
    """

    ext = os.path.splitext(filename)[1] if extension_hint is None else extension_hint

    if ext == ".geogram":
        return Mesh(PyMesh.load_geogram_mesh(filename))
    if not os.path.exists(filename):
        raise IOError("File not found: {}".format(filename))
    factory = PyMesh.MeshFactory()
    if extension_hint is None:
        factory.load_file(filename)
    else:
        factory.load_file_with_hint(filename, extension_hint)
    if drop_zero_dim:
        factory.drop_zero_dim()
    return Mesh(factory.create())


def deduce_face_type(faces, voxels):
    if faces is None or faces.ndim == 1 or len(faces) == 0:
        assert voxels is not None and voxels.ndim == 2
        if voxels.shape[1] == 4:
            faces = np.zeros((0, 3))
        elif voxels.shape[1] == 8:
            faces = np.zeros((0, 4))
        elif len(voxels) == 0:
            faces = np.zeros((0, 3))
        else:
            raise NotImplementedError("Face type cannot be deduced from voxel.")
    return faces


def deduce_voxel_type(faces, voxels):
    if voxels is None or voxels.ndim == 1 or len(voxels) == 0:
        assert faces.ndim == 2
        if faces.shape[1] == 3:
            voxels = np.zeros((0, 4))
        elif faces.shape[1] == 4:
            voxels = np.zeros((0, 8))
        elif len(faces) == 0:
            voxels = np.zeros((0, 4))
        else:
            raise NotImplementedError("Voxel type cannot be deduced from face.")
    return voxels


def form_mesh(vertices, faces, voxels=None):
    """Convert raw mesh data into a Mesh object.

    Args:
        vertices (`numpy.ndarray`): ndarray of floats with size (num_vertices,
            dim).
        faces: ndarray of ints with size (num_faces, vertex_per_face).
        voxels: optional ndarray of ints with size (num_voxels,
            vertex_per_voxel).  Use ``None`` for forming surface meshes.

    Returns:
        A :py:class:`Mesh` object formed by the inputs.

    Example:

        >>> vertices = np.array([
        ...     [0.0, 0.0],
        ...     [1.0, 0.0],
        ...     [1.0, 1.0],
        ...     [0.0, 1.0],
        ...     ])
        >>> faces = np.array([
        ...     [0, 1, 2],
        ...     [0, 2, 3],
        ...     ])
        >>> mesh = pymesh.form_mesh(vertices, faces)
    """
    voxels = deduce_voxel_type(faces, voxels)
    faces = deduce_face_type(faces, voxels)

    factory = PyMesh.MeshFactory()
    factory.load_matrices(vertices, faces, voxels)
    return Mesh(factory.create())


def save_mesh_raw(filename, vertices, faces, voxels=None, **setting):
    """Save raw mesh to file.

    Args:
        filename (:py:class:`str`): Output file.  File format is auto detected from extension.
        vertices (:py:class:`numpy.ndarray`): Array of floats with size (num_vertices, dim).
        faces (:py:class:`numpy.ndarray`): Arrayof ints with size (num_faces, vertex_per_face).
        voxels (:py:class:`numpy.ndarray`): (optional) ndarray of ints with size (num_voxels,
            vertex_per_voxel).  Use ``None`` for forming surface meshes.
        **setting (:py:class:`dict`): (optional) The following keys are recognized.

            * ascii: whether to use ascii encoding, default is false.
            * use_float: store scalars as float instead of double, default is
              false.
            * anonymous: whether to indicate the file is generated by PyMesh.

    Example:

        >>> mesh = pymesh.generate_regular_tetrahedron()
        >>> pymesh.save_mesh_raw("out.msh",
        ...         mesh.vertices, mesh.faces, mesh.voxels)
    """
    voxels = deduce_voxel_type(faces, voxels)
    faces = deduce_face_type(faces, voxels)

    if not isinstance(vertices, np.ndarray):
        vertices = np.array(vertices, copy=False, order="C")
    if not isinstance(faces, np.ndarray):
        faces = np.array(faces, copy=False, order="C")
    if not isinstance(voxels, np.ndarray):
        voxels = np.array(voxels, copy=False, order="C")

    dim = vertices.shape[1]
    num_vertex_per_face = faces.shape[1]
    num_vertex_per_voxel = voxels.shape[1]

    writer = PyMesh.MeshWriter.create(filename)
    if setting.get("ascii", False):
        writer.in_ascii()
    if setting.get("use_float", False):
        writer.use_float()
    writer.write(
        vertices.ravel(order="C"),
        faces.ravel(order="C"),
        voxels.ravel(order="C"),
        dim,
        num_vertex_per_face,
        num_vertex_per_voxel,
    )


def save_mesh(filename, mesh, *attributes, **setting):
    """Save mesh to file.

    Args:
        filename (:py:class:`str`): Output file.  File format is auto detected from extension.
        mesh (:py:class:`Mesh`): Mesh object.
        *attributes (:py:class:`list`): (optional) Attribute names to be saved.
            This field would be ignored if the output format does not support
            attributes (e.g. **.obj** and **.stl** files)
        **setting (:py:class:`dict`): (optional) The following keys are recognized.

            * ascii: whether to use ascii encoding, default is false.
            * use_float: store scalars as float instead of double, default is
              false.
            * anonymous: whether to indicate the file is generated by PyMesh.

    Raises:
        KeyError: Attributes cannot be found in mesh.

    Example:

        >>> box = pymesh.generate_box_mesh()
        >>> pymesh.save_mesh("tmp.stl", box, ascii=True)
    """
    ext = os.path.splitext(filename)[1]
    if ext == ".geogram":
        PyMesh.save_geogram_mesh(filename, mesh.raw_mesh)
        return
    elif ext == ".svg":
        save_svg(filename, mesh)
        return
    writer = PyMesh.MeshWriter.create(filename)
    for attr in attributes:
        if not mesh.has_attribute(attr):
            raise KeyError("Attribute {} is not found in mesh".format(attr))
        writer.with_attribute(attr)
    if setting.get("ascii", False):
        writer.in_ascii()
    if setting.get("use_float", False):
        writer.use_float()
    if setting.get("anonymous", False):
        writer.set_anonymous()
    writer.write_mesh(mesh.raw_mesh)
