import pygame
from Snake import Snake
from Arena import Arena
from Game_Manager import GameManager
from Score import Score

def main():
    pygame.init()

    # Paramètres du jeu
    width, height = 20, 20
    cell_size = 20
    screen = pygame.display.set_mode((width * cell_size, height * cell_size + 40))  # Ajout d'espace pour les scores
    pygame.display.set_caption("Snake Multiplayer")
    clock = pygame.time.Clock()

    # Police pour les scores
    score_font = pygame.font.SysFont(None, 30)

    # Initialisation
    arena = Arena(width, height)
    snake1 = Snake((5, 5), "RIGHT", (0, 255, 0))
    snake2 = Snake((10, 10), "LEFT", (0, 0, 255))
    snakes = [snake1, snake2]
    arena.generate_food(snakes)
    game_manager = GameManager(arena, snakes)

    running = True

    while running:
        game_over = False

        # Boucle principale du jeu
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True

            # Gestion des touches
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                snake1.direction = "UP"
            elif keys[pygame.K_DOWN]:
                snake1.direction = "DOWN"
            elif keys[pygame.K_LEFT]:
                snake1.direction = "LEFT"
            elif keys[pygame.K_RIGHT]:
                snake1.direction = "RIGHT"

            if keys[pygame.K_w]:
                snake2.direction = "UP"
            elif keys[pygame.K_s]:
                snake2.direction = "DOWN"
            elif keys[pygame.K_a]:
                snake2.direction = "LEFT"
            elif keys[pygame.K_d]:
                snake2.direction = "RIGHT"

            # Gestion du jeu
            game_manager.next_turn()
            if game_manager.is_game_over():
                game_over = True

            # Affichage
            game_manager.draw(screen, cell_size)

            # Affichage des scores
            screen.fill((0, 0, 0), pygame.Rect(0, height * cell_size, width * cell_size, 40))
            
            # Score du Snake 1 (Vert)
            score1_text = score_font.render(f"Player 1: {snake1.score.get_current_score()} (High: {snake1.score.get_high_score()})", True, (0, 255, 0))
            screen.blit(score1_text, (10, height * cell_size + 10))

            # Score du Snake 2 (Bleu)
            score2_text = score_font.render(f"Player 2: {snake2.score.get_current_score()} (High: {snake2.score.get_high_score()})", True, (0, 0, 255))
            screen.blit(score2_text, (width * cell_size // 2 + 10, height * cell_size + 10))

            pygame.display.flip()
            clock.tick(10)

        # Écran Game Over
        while game_over and running:
            screen.fill((0, 0, 0))
            
            # Déterminer le gagnant
            winner = "Égalité"
            if snake1.score.get_current_score() > snake2.score.get_current_score():
                winner = "Joueur 1 (Vert)"
            elif snake2.score.get_current_score() > snake1.score.get_current_score():
                winner = "Joueur 2 (Bleu)"

            # Textes Game Over
            font_title = pygame.font.SysFont(None, 36)
            font_details = pygame.font.SysFont(None, 25)
            
            title_text = font_title.render("Game Over!", True, (255, 255, 255))
            winner_text = font_details.render(f"Gagnant: {winner}", True, (255, 255, 255))
            score1_text = font_details.render(f"Joueur 1: {snake1.score.get_current_score()} (High: {snake1.score.get_high_score()})", True, (0, 255, 0))
            score2_text = font_details.render(f"Joueur 2: {snake2.score.get_current_score()} (High: {snake2.score.get_high_score()})", True, (0, 0, 255))
            restart_text = font_details.render("Press R to restart or Q to quit.", True, (255, 255, 255))

            screen.blit(title_text, (width * cell_size // 2 - 50, height * cell_size // 2 - 60))
            screen.blit(winner_text, (width * cell_size // 2 - 50, height * cell_size // 2 - 30))
            screen.blit(score1_text, (width * cell_size // 2 - 100, height * cell_size // 2))
            screen.blit(score2_text, (width * cell_size // 2 - 100, height * cell_size // 2 + 30))
            screen.blit(restart_text, (width * cell_size // 2 - 100, height * cell_size // 2 + 60))
            
            pygame.display.flip()

            # Attente des instructions utilisateur
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Rejouer
                        # Recréer les snakes avec leurs scores conservés
                        snake1 = Snake((5, 5), "RIGHT", (0, 255, 0))
                        snake2 = Snake((10, 10), "LEFT", (0, 0, 255))
                        game_manager = GameManager(arena, [snake1, snake2])
                        arena.generate_food(game_manager.snakes)
                        game_over = False  # Quitte l'état "Game Over"
                    elif event.key == pygame.K_q:  # Quitter
                        running = False
                        game_over = True

    pygame.quit()

if __name__ == "__main__":
    main()