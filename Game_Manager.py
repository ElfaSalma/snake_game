class GameManager:
    """
    Gère le déroulement du jeu, les tours et les collisions.
    """
    def __init__(self, arena, snakes):
        self.arena = arena
        self.snakes = snakes
        self.current_player = 0

    def next_turn(self):
        """
        Gère le tour du joueur actif.
        """
        current_snake = self.snakes[self.current_player]

        if current_snake.alive:
            current_snake.move()
            current_snake.check_collision(self.arena)

            # Vérifier si le serpent mange de la nourriture
            if current_snake.body[0] == self.arena.food:
                current_snake.grow()
                current_snake.score.increase()  # Augmente le score
                self.arena.generate_food(self.snakes)

        # Passer au prochain joueur
        self.current_player = (self.current_player + 1) % len(self.snakes)

    def is_game_over(self):
        """
        Vérifie si tous les serpents sont morts.
        """
        return all(not snake.alive for snake in self.snakes)

    def draw(self, screen, cell_size):
        """
        Affiche l'état actuel de l'arène et des serpents.
        """
        self.arena.draw(screen, cell_size)
        for snake in self.snakes:
            snake.draw(screen, cell_size)
            
    def reset(self):
        """
        Réinitialise l'état du jeu pour recommencer.
        """
        for snake in self.snakes:
            snake.body = [snake.body[0]]  # Réinitialise les positions des serpents
            snake.alive = True
            snake.score.reset()  # Réinitialise le score
        self.current_player = 0
        self.arena.generate_food(self.snakes)