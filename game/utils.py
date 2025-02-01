def project_4d_to_3d(vertex):
    x, y, z, w = vertex
    # Simple projection: drop the w coordinate
    return (x, y, z)