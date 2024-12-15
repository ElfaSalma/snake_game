import pygame
from Score import Score

# Classe Snake 
class Snake:
    """
    Représente un serpent, ses mouvements et son état.
    """
    def __init__(self, start_pos, direction, color):
        self.body = [start_pos]
        self.direction = direction
        self.color = color
        self.alive = True
        self.score = Score(self)  # Ajout de l'initialisation du score

    def move(self):
        """
        Fait avancer le serpent dans sa direction actuelle.
        """
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        else:
            return

        self.body = [new_head] + self.body[:-1]

    def grow(self):
        """
        Ajoute une nouvelle cellule au corps du serpent.
        """
        self.body.append(self.body[-1])

    def check_collision(self, arena):
        """
        Vérifie si le serpent entre en collision avec un mur ou lui-même.
        """
        head_x, head_y = self.body[0]

        # Collision avec les murs
        if head_x < 0 or head_x >= arena.width or head_y < 0 or head_y >= arena.height:
            self.alive = False

        # Collision avec son propre corps
        if self.body[0] in self.body[1:]:
            self.alive = False

    def draw(self, screen, cell_size):
        """
        Affiche le serpent.
        """
        for segment in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))