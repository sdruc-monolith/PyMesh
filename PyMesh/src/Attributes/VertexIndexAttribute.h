/* This file is part of PyMesh. Copyright (c) 2015 by Qingnan Zhou */
#pragma once

#include "MeshAttribute.h"

namespace PyMesh {

class VertexIndexAttribute : public MeshAttribute {
    public:
        virtual ~VertexIndexAttribute() = default;

    public:
        virtual void compute_from_mesh(Mesh& mesh) override;
};

}