# Treasure Hunt Game

## Project Introduction
"Treasure Hunt" is a 2D grid-based treasure hunting game. Players use the up, down, left, and right keys to control the character to find three hidden treasures on the map and avoid obstacles. The game map is randomly generated at each startup to ensure that each game is unique. Players gradually find treasures by moving on the map while avoiding obstacles.

## How to Run the Game

### System Requirements
- Java version: JDK 23 version is required.
- IDE: IntelliJ IDEA is recommended.

## Game Features
- Players start with 100 points, and each move consumes 1 point and 1 gold coin.
- **Map Generation**: The game map is a 20x20 two-dimensional grid containing obstacles, empty paths and treasures. The map is randomly generated in each game.
- **Player Movement**: Players can move up, down, left, and right.
- **Treasure**: The player's goal is to find three treasures on the map. For each treasure found, the player will receive a 20-point bonus.
- **Obstacle**: The player must avoid hitting obstacles, otherwise he will lose 10 points.
- **Hint function**: When the player's score is less than 60 points, the game will remind the player to use the hint function. Each use of the hint function will consume 3 points. Players can use hints to see the next step to reach the treasure.
- **Add points function**: When the player's score is less than 10 points, the system only allows the player to add points once, providing a 20-point bonus to help the player continue the game.
- **Ranking**: The game can record the top 5 points and display the player's achievements.
- **Background music control**: Players can choose to turn off the background music to reduce game interference.
- **Developer mode**: Game developers can click the space bar to view the shortest path to the treasure and test the effectiveness of the algorithm.
- **Exit game**: In the game, players can select the cancel button to end the current game.
- **Restart the game**: During the game, players can select the restart button to restart the game.