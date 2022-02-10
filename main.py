import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum")

g = 0.4


font = pygame.font.Font("FiraCode-Medium.ttf", 40)
text_surface = font.render("", True, (10, 10, 10))
graph_surface = pygame.Surface(size=(WIDTH, HEIGHT))
graph_surface.set_colorkey((0, 0, 0))

x = 0


class Pendulum:
    def __init__(self, length, source_pos, vel, theta, mu):
        self.source_pos = source_pos
        self.vel = vel
        self.length = length
        self.theta = theta
        self.acc = (-g / self.length) * math.sin(self.theta)
        self.mu = mu

    def update_theta(self):
        self.acc = (-g / self.length) * math.sin(self.theta)
        self.vel += self.acc
        self.theta += self.vel

    def draw_pendulum(self):
        global text_surface
        global x

        position = (self.length*math.sin(self.theta) + self.source_pos[0],
                    self.length*math.cos(self.theta) + self.source_pos[1])
        pygame.draw.line(WIN, (100, 100, 100), self.source_pos, position, 4)

        pygame.draw.circle(
            WIN, "#008080",
            position,
            16
        )

        text_surface = font.render(f"θ: {round(self.theta*180/math.pi)}°", True, (10, 10, 10))
        pygame.draw.circle(graph_surface, (1, 1, 1), (x, self.theta*180/math.pi + 250), 3)
        x += 1


def main():
    clock = pygame.time.Clock()
    pendulum = Pendulum(200, (WIDTH/2, 250), 0.03, math.pi, 0.005)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill((255, 255, 255))
        pendulum.update_theta()
        pendulum.draw_pendulum()
        # WIN.blit(graph_surface, (0, 0))
        WIN.blit(text_surface, (10, 10))
        pygame.display.update()


main()
pygame.quit()
