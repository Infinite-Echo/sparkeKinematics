import sympy as sym

def create_base_transformation(x_base, y_base, z_base, roll, pitch, yaw):
    rotxyz = create_rot_xyz(roll, pitch, yaw)
    Tbase = create_base_translation(x_base, y_base, z_base)
    Tm = rotxyz*Tbase
    return Tm

def create_base_translation(x_base, y_base, z_base):
    Tbase = sym.Matrix([
        [1, 0, 0, x_base],
        [0, 1, 0, y_base],
        [0, 0, 1, z_base],
        [0, 0, 0, 1],
    ])
    return Tbase

def create_rot_xyz(roll, pitch, yaw):
    rotx = create_rotx(roll)
    roty = create_roty(pitch)
    rotz = create_rotz(yaw)
    rotxy = rotx*roty
    rotxyz = rotxy*rotz
    return rotxyz

def create_rotx(roll):
    rotx = sym.Matrix([
        [1, 0, 0, 0],
        [0, sym.cos(roll), -sym.sin(roll), 0],
        [0, sym.sin(roll), sym.cos(roll), 0],
        [0, 0, 0, 1],
    ])
    return rotx

def create_roty(pitch):
    roty = sym.Matrix([
        [sym.cos(pitch), 0, -sym.sin(pitch), 0],
        [0, 1, 0, 0],
        [sym.sin(pitch), 0, sym.cos(pitch), 0],
        [0, 0, 0, 1],
    ])
    return roty

def create_rotz(yaw):
    rotz = sym.Matrix([
        [sym.cos(yaw), -sym.sin(yaw), 0, 0],
        [sym.sin(yaw), sym.cos(yaw), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    return rotz