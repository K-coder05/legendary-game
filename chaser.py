import pygame

class Chaser():
    def __init__(self, position, position_chase, velocity, image):
        self.__position = position
        self.__position_chase = position_chase
        self.__velocity = velocity
        self.__image = image

    def chase_mechanic(self, position, position_chase):
        distance_x = abs(position.x - position_chase.x)
        distance_y = abs(position.y - position_chase.y)

        if distance_x > distance_y:
            if (position.x < position_chase.x):
                position_chase.x -= self.__velocity
            else:
                position_chase.x += self.__velocity
        else:
            if (position.y < position_chase.y):
                position_chase.y -= self.__velocity
            else:
                position_chase.y += self.__velocity

    def draw(self, WIN):
        WIN.blit(self.__image, (self.__position_chase.x, self.__position_chase.y))
