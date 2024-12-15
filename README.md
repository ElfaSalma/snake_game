# Multi-Snake Game

**Multi-Snake Game** est une version multijoueur du célèbre jeu **Snake**, développée en Python avec Pygame. Ce projet propose une expérience unique où deux joueurs s'affrontent dans une arène avec des mécaniques de tour par tour.

## 🎮 Fonctionnalités

- **Multijoueur local** : Jusqu'à 2 joueurs peuvent jouer ensemble sur le même clavier.
- **Tour par tour** : Les joueurs jouent à tour de rôle, ajoutant une touche stratégique au gameplay.
- **Arène avec obstacles** : Les murs délimitent l'arène, et les collisions sont mortelles.
- **Mécanique de nourriture** : Les serpents mangent pour grandir et augmenter leur score.
- **Gestion des collisions** : Les serpents meurent en cas de collision avec un mur, un autre serpent, ou eux-mêmes.
- **Menu de redémarrage** : Après un "Game Over", les joueurs peuvent choisir de rejouer ou de quitter le jeu.
- **Premier serpent (vert)** : Touches fléchées (HAUT, BAS, GAUCHE, DROITE)
- **Deuxième serpent (bleu)** : Touches W, A, S, D
      
      - W : Se déplacer VERS LE HAUT
      - S : Se déplacer VERS LE BAS
      - A : Se déplacer VERS LA GAUCHE
      - D : Se déplacer VERS LA DROITE

## 🛠️ Technologies utilisées

- **Python** : Langage de programmation principal.
- **Pygame** : Bibliothèque utilisée pour la gestion graphique et les interactions.

## 🚀 Comment exécuter le projet

### Prérequis

- Python 3.x installé sur votre système.
- Pygame installé via pip :

  ```bash
  pip install pygame
  ```

### Étapes pour lancer le jeu

1. Clonez ce dépôt GitHub sur votre machine locale :
   ```bash
   git clone https://github.com/ElfaSalma/snake_game.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd snake_game
   ```
3. Exécutez le fichier principal :
   ```bash
   python main.py
   ```

## 🎯 Règles du jeu

1. Les joueurs se déplacent à tour de rôle dans une arène délimitée par des murs.
2. Si un joueur meurt (collision avec un mur, un autre serpent, ou son propre corps), il est éliminé.
3. Le jeu continue jusqu'à ce que tous les serpents soient morts.
4. Un menu "Game Over" s'affiche, offrant la possibilité de rejouer ou de quitter.

## 💡 Améliorations futures

- **Modes de jeu supplémentaires** : Ajout d'un mode temps réel ou d'une arène dynamique.
- **Multijoueur en réseau** : Permettre à des joueurs distants de s'affronter.
- **Personnalisation des serpents** : Couleurs, tailles et skins variés.
- **Enregistrement des scores** : Sauvegarder les meilleurs scores pour chaque joueur.

## 🖼️ Aperçu
Voici à quoi ressemble le jeu en cours d'exécution :

![Capture du jeu](image/capture-jeu.png)


## 🧑‍💻 Auteur

- **Salma Elfa**

N'hésitez pas à me contacter via GitHub pour toute question ou suggestion d'amélioration.


