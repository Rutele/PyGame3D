import numpy as np
import os


class DObject(object):
    vertices = None
    visible_vertices = None
    pivot = None
    faces = None
    visible_faces = None

    def __init__(self):
        self.vertices, self.faces = obj_parser()
        self.visible_vertices = []
        self.iso_projection()
        self.pivot = np.mean(self.vertices, axis=0)
        self.visible_faces = self.d_faces()

    def d_faces(self):
        point_list = []
        for face in self.faces:
            point_list.append([self.visible_vertices[face[0] - 1], self.visible_vertices[face[1] - 1],
                               self.visible_vertices[face[2] - 1], self.visible_vertices[face[3] - 1]])
        return point_list

    def iso_projection(self):
        projection_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        iso_matrix = (1 / np.sqrt(6)) * np.array([[np.sqrt(3), 0, -np.sqrt(3)], [1, 2, 1], [np.sqrt(2), -np.sqrt(2),
                                                  np.sqrt(2)]])

        for vertex in self.vertices:
            vertex = np.vstack(vertex)
            c_matrix = np.dot(iso_matrix, vertex)
            vertex = np.dot(projection_matrix, c_matrix)
            vertex = np.hstack(vertex)
            self.visible_vertices.append(vertex)

    def disp(self):
        points = []
        vertices = []
        for face in self.visible_faces:
            for i, vertex in enumerate(face):
                if (i + 1) % 4 == 0:
                    points.append(vertices)
                    vertices = []
                else:
                    vertices.append(tuple([vertex[0], vertex[1]]))
        return points

    def translate_x(self):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = [vertex[0] + 1, vertex[1], vertex[2]]
            print(vertex)
        self.visible_vertices = []
        self.iso_projection()
        self.pivot = np.mean(self.vertices, axis=0)
        self.visible_faces = self.d_faces()


class Cube(DObject):

    def __init__(self):
        super().__init__()


def obj_parser():
    current_path = os.path.dirname(__file__)
    file = os.path.join(current_path, 'untitled.obj')
    vertices_list = []
    faces_list = []

    with open(file, 'r') as source:
        for line in source:
            line = line.split()
            if line[0] == 'f':
                faces_list.append([int(line[1][0]), int(line[2][0]),
                                   int(line[3][0]), int(line[4][0])])
            elif line[0] == 'v':
                vertices_list.append(np.array([int(line[1]), int(line[2]), int(line[3])]))

    return vertices_list, faces_list
