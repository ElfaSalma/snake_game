import random
import pygame

# Classe Arena 
class Arena:
    """
    Gère l'arène, les murs et la nourriture.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.food = None

    def generate_food(self, snakes):
        """
        Génère de la nourriture à une position aléatoire qui n'est pas occupée par un serpent.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if all((x, y) not in snake.body for snake in snakes):
                self.food = (x, y)
                break

    def draw(self, screen, cell_size):
        """
        Affiche l'arène, les murs et la nourriture.
        """
        screen.fill((0, 0, 0))  # Fond noir

        # Dessiner les murs (bordures)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, self.width * cell_size, cell_size))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, cell_size, self.height * cell_size))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((self.width - 1) * cell_size, 0, cell_size, self.height * cell_size))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, (self.height - 1) * cell_size, self.width * cell_size, cell_size))

        # Dessiner la nourriture
        if self.food:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.food[0] * cell_size, self.food[1] * cell_size, cell_size, cell_size))
            
