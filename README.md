# 🐍 Snake Agent

Welcome to my **Snake Agent** project! This project explores how a neural network can learn to play the classic game of **Snake**, with the end goal of implementing both a **software-based AI agent** and a **hardware-based FPGA implementation**.

## 🎯 Project Goals

- Implement a Deep Q-Network (DQN) to learn how to play Snake using reinforcement learning in Python.
- Visualize the learning process and game performance over time.
- Translate the trained neural network into a **hardware-friendly format** and implement it in **Verilog** on an FPGA (e.g., Basys3).
- Build a **fully autonomous Snake-playing system** that runs independently on FPGA hardware.

## 🧠 AI Overview

This project uses a **Deep Q-Network (DQN)**:
- **State representation**: Encodes the game state (e.g., direction, food position, tail danger).
- **Action space**: [Straight, Turn Left, Turn Right].
- **Reward structure**: Positive reward for eating food, negative for dying, small penalty per time step to encourage efficiency.
- **Learning framework**: 
  - Experience replay
  - Epsilon-greedy exploration
  - Neural network for Q-value approximation

The training is done in Python using frameworks such as **PyTorch** or **TensorFlow**. In this project, I will use PyTorch due to it being easy to pick up.

## 🕹️ Game Environment

The Snake game is implemented in Python using **Pygame**. The AI agent interacts with the environment by:
- Observing the current state of the game.
- Choosing an action based on its learned Q-values.
- Receiving rewards and updating its policy.

## Basic Theory

Reinforcement learning (RL) is a subfield of machine learning focused on training software agents to make sequences of decisions by interacting with an environment. The primary objective of these agents is to learn a policy that maximizes cumulative reward over time. Unlike supervised learning, where the model learns from a dataset of labeled examples, reinforcement learning involves learning from the consequences of actions taken in an environment.
<br />
Key components of reinforcement learning include:

- Agent: The learner or decision-maker that interacts with the environment.
- Environment: The external system with which the agent interacts. It provides feedback in the form of rewards or penalties based on the agent's actions.
- State: A representation of the current situation of the environment. The agent uses this information to decide on the next action.
- Action: A decision made by the agent that affects the state of the environment.
- Reward: A scalar value received by the agent after taking an action, indicating the immediate benefit of that action. The goal of the agent is to maximize the cumulative    reward over time.
- Policy: A strategy or mapping from states to actions that the agent follows. The policy can be deterministic or stochastic.
- Value Function: A function that estimates the expected cumulative reward from a given state or state-action pair, helping the agent evaluate the long-term benefit of        actions.
-- Exploration vs. Exploitation: A trade-off the agent must manage between exploring new actions to discover their effects and exploiting known actions that yield high         rewards.

---

This README is just a summary of the project at a high level, please go into both the `Python` and `Verilog` submodules to read more in depth about the lower level implementation.

