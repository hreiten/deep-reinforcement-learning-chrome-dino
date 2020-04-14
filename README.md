# Deep Q-learning of Chrome's dinosaur game

The aim of this repo is to teach [Chrome's offline dinosaur](chrome://dino/) when to jump using deep reinforcement learning.
This is an implementation of the algorithm proposed in [this research article](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf), where a Deep Concolutional Neural Network takes pure pixel inputs of the game as inputs to predict actions for the agent.

Some practical implementations that have been used for inspiration:

- https://pythonprogramming.net/deep-q-learning-dqn-reinforcement-learning-python-tutorial/
- https://blog.paperspace.com/dino-run/

## Description and implementation

/_ TODO _/

## Setup and installation

Make sure you have the following installed before you proceed:

- [Pipenv](https://github.com/pypa/pipenv)
- Python v3.7
- Google Chrome

Steps:

1. Clone or fork this repository
2. Install packages and enter virtual env:

```
pipenv install --skip-lock
pipenv shell
```

3. Start jupyter session

```
jupyter lab
```

4. Open `dino-trainer.ipynb` to start coding!

## Repository overview

- `dino-trainer.ipynb` contains all code to run the game and train the CNN
- `visualize.ipynb` is a notebook to show and analyse statistics from the training process.
- `helpers.py` defines utility functions used in `dino-trainer.ipynb`
