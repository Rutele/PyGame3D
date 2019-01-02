import pygame
import numpy as np

pygame.init()
running = True
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()

colour_1 = (255, 255, 255)
colour_2 = (255, 0, 255)

vertex_1 = np.array([100, 100, 0])
vertex_2 = np.array([200, 100, 0])
vertex_3 = np.array([200, 200, 0])
vertex_4 = np.array([100, 200, 0])

vertex_5 = np.array([100, 100, 100])
vertex_6 = np.array([200, 100, 100])
vertex_7 = np.array([200, 200, 100])
vertex_8 = np.array([100, 200, 100])


def projection(vertex):
    """
    alpha = np.deg2rad(35.264)
    beta = np.deg2rad(45)
    """
    projection_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    iso_matrix = (1/np.sqrt(6)) * np.array([[np.sqrt(3), 0, -np.sqrt(3)], [1, 2, 1], [np.sqrt(2), -np.sqrt(2), np.sqrt(2)]])
    vertex = np.vstack(vertex)
    c_matrix = np.dot(iso_matrix, vertex)
    vertex = np.dot(projection_matrix, c_matrix)
    vertex = np.hstack(vertex)
    vertex = np.delete(vertex, 2)
    return vertex


def rotation_x(vertex, angle):
    trans_vector = np.array([150, 150, 50])
    angle = np.deg2rad(angle)
    trans_matrix = np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])

    vertex = vertex - trans_vector
    vertex = np.vstack(vertex)
    vertex = np.dot(trans_matrix, vertex)

    vertex = np.hstack(vertex)
    vertex = vertex + trans_vector
    return vertex


def rotation_y(vertex, angle):
    trans_vector = np.array([150, 150, 50])
    angle = np.deg2rad(angle)
    trans_matrix = np.array([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])

    vertex = vertex - trans_vector
    vertex = np.vstack(vertex)
    vertex = np.dot(trans_matrix, vertex)

    vertex = np.hstack(vertex)
    vertex = vertex + trans_vector
    return vertex


def rotation_z(vertex, angle):
    trans_vector = np.array([150, 150, 50])
    angle = np.deg2rad(angle)
    trans_matrix = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

    vertex = vertex - trans_vector
    vertex = np.vstack(vertex)
    vertex = np.dot(trans_matrix, vertex)

    vertex = np.hstack(vertex)
    vertex = vertex + trans_vector
    return vertex


alpha = 0
beta = 0
gamma = 0
while running:
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, colour_2, projection(vertex_1), projection(vertex_2))
    pygame.draw.line(screen, colour_2, projection(vertex_2), projection(vertex_3))
    pygame.draw.line(screen, colour_2, projection(vertex_3), projection(vertex_4))
    pygame.draw.line(screen, colour_2, projection(vertex_4), projection(vertex_1))

    pygame.draw.line(screen, colour_2, projection(vertex_5), projection(vertex_6))
    pygame.draw.line(screen, colour_2, projection(vertex_6), projection(vertex_7))
    pygame.draw.line(screen, colour_2, projection(vertex_7), projection(vertex_8))
    pygame.draw.line(screen, colour_2, projection(vertex_8), projection(vertex_5))

    pygame.draw.line(screen, colour_2, projection(vertex_1), projection(vertex_5))
    pygame.draw.line(screen, colour_2, projection(vertex_2), projection(vertex_6))
    pygame.draw.line(screen, colour_2, projection(vertex_3), projection(vertex_7))
    pygame.draw.line(screen, colour_2, projection(vertex_4), projection(vertex_8))

    """
    pygame.draw.line(screen, colour_1, np.delete(vertex_1, 2), np.delete(vertex_2, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_2, 2), np.delete(vertex_3, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_3, 2), np.delete(vertex_4, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_4, 2), np.delete(vertex_1, 2))

    pygame.draw.line(screen, colour_1, np.delete(vertex_5, 2), np.delete(vertex_6, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_6, 2), np.delete(vertex_7, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_7, 2), np.delete(vertex_8, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_8, 2), np.delete(vertex_5, 2))

    pygame.draw.line(screen, colour_1, np.delete(vertex_1, 2), np.delete(vertex_5, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_2, 2), np.delete(vertex_6, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_3, 2), np.delete(vertex_7, 2))
    pygame.draw.line(screen, colour_1, np.delete(vertex_4, 2), np.delete(vertex_8, 2))
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        alpha = alpha + 1
        vertex_1 = rotation_x(vertex_1, 1)
        vertex_2 = rotation_x(vertex_2, 1)
        vertex_3 = rotation_x(vertex_3, 1)
        vertex_4 = rotation_x(vertex_4, 1)
        vertex_5 = rotation_x(vertex_5, 1)
        vertex_6 = rotation_x(vertex_6, 1)
        vertex_7 = rotation_x(vertex_7, 1)
        vertex_8 = rotation_x(vertex_8, 1)
        print(alpha)
    if keys[pygame.K_e]:
        beta = beta + 1
        vertex_1 = rotation_y(vertex_1, 1)
        vertex_2 = rotation_y(vertex_2, 1)
        vertex_3 = rotation_y(vertex_3, 1)
        vertex_4 = rotation_y(vertex_4, 1)
        vertex_5 = rotation_y(vertex_5, 1)
        vertex_6 = rotation_y(vertex_6, 1)
        vertex_7 = rotation_y(vertex_7, 1)
        vertex_8 = rotation_y(vertex_8, 1)
    if keys[pygame.K_w]:
        gamma = gamma + 1
        vertex_1 = rotation_z(vertex_1, 1)
        vertex_2 = rotation_z(vertex_2, 1)
        vertex_3 = rotation_z(vertex_3, 1)
        vertex_4 = rotation_z(vertex_4, 1)
        vertex_5 = rotation_z(vertex_5, 1)
        vertex_6 = rotation_z(vertex_6, 1)
        vertex_7 = rotation_z(vertex_7, 1)
        vertex_8 = rotation_z(vertex_8, 1)

    pygame.display.update()
    clock.tick(30)
