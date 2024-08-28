# Deep Learning Tetris AI
This tetris project is a fork of Rex L.'s deep learning Tetris agent, aimed to optimize the deep learning algorithm. A link to the original project can be found below:

https://github.com/zeroize318/tetris_ai

A thesis was written for this project on how the deep learning algorithm works, with my approach's benefits over the original code proven. This thesis can be found in the repo as "Optimizing Tetris with Deep Reinforcement Learning".

Below are the instructions written by Rex L. on how to run the project:

# AI plays custom Tetris
## Requirement:
tensorflow [probably v2.5]

## Usage:
1. edit "common.py";
   
   choose mode "human_player", "ai_player_training" and "ai_player_watching"
2. edit "tetromino.py" -> create_pool(cls): -> elif GAME_TYPE == 'extra':
    
    add or delete tetromino.
3. run "tetris_ai.py".

    training may take a significant amount of cpu usage.

## Links:
[Example video](https://youtu.be/FTDZN4pPhwA)

[Article on Medium](https://rex-l.medium.com/reinforcement-learning-on-tetris-707f75716c37)



    
