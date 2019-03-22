from pyglet.gl import *


Vector = GLfloat * 3


class Loader:
    def __init__(self, filename, swapyz=False):
        """ Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.faces = []

        for line in open(filename, "r"):
            if line.startswith('#'):
                continue

            values = line.split()
            if not values:
                continue

            if values[0] == 'v':
                v = [float(i) for i in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = [float(i) for i in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'f':
                face = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms))

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)

        glFrontFace(GL_CCW)
        for face in self.faces:
            vertices, normals = face
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3f(*self.normals[normals[i] - 1])
                glVertex3f(*self.vertices[vertices[i] - 1])
            glEnd()
        glEndList()

    def draw(self):
        glCallList(self.gl_list)
