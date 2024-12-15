class Score:
    """
    Gère le score des serpents dans le jeu.
    """
    def __init__(self, snake):
        """
        Initialise le score pour un serpent donné.
        
        :param snake: L'instance du serpent associée à ce score
        """
        self.snake = snake
        self.current_score = 0
        self.high_score = 0

    def increase(self, points=1):
        """
        Augmente le score du serpent.
        
        :param points: Nombre de points à ajouter (défaut: 1)
        """
        self.current_score += points
        # Mettre à jour le high score si nécessaire
        self.high_score = max(self.high_score, self.current_score)

    def reset(self):
        """
        Réinitialise le score courant tout en conservant le high score.
        """
        self.current_score = 0

    def get_current_score(self):
        """
        Renvoie le score courant du serpent.
        
        :return: Score courant
        """
        return self.current_score

    def get_high_score(self):
        """
        Renvoie le high score du serpent.
        
        :return: High score
        """
        return self.high_score