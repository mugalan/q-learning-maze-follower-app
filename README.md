<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Q-Learning Maze Follower App</h1>
  <p>This Python app uses Q-learning to find the optimal path through a maze. It is built with the Plotly and Dash frameworks.</p>

  <h2>Features</h2>
  <ul>
    <li>Maze editor: create your own custom maze to run the algorithm on.</li>
    <li>Q-learning algorithm: uses reinforcement learning to find the optimal path through the maze.</li>
    <li>Visualization: view the maze and the optimal path through it in real-time.</li>
    <li>Dynamic/animated simulation: watch the Q-learning algorithm find the optimal path through the maze in real-time.</li>
    <li>Obstacle editor: add or remove obstacles to the path of the follower.</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository: <code>git clone https://github.com/DinithHeshan/q-learning-maze-follower-app.git</code></li>
    <li>Install the required packages: <code>pip install -r requirements.txt</code></li>
  </ol>

  <h2>Usage</h2>
  <ol>
    <li>Run the app: <code>Maze_Follower_App.py</code></li>
    <li>Select the maze size by using the "Grid Size" input.</li>
    <li>Add or remove walls by clicking on the maze squares.</li>
    <li>Select the destination square by clicking on a square and then clicking the "Set Destination" button.</li>
    <li>Choose the algorithm parameters (discount factor, greedy policy, and learning rate) using the respective inputs.</li>
    <li>Train the algorithm by clicking the "Train" button, choosing the number of episodes, and clicking "Start Training".</li>
    <li>Watch the algorithm train in real-time, with the number of trained episodes displayed.</li>
    <li>Select the initial point for the follower by clicking on a square and then clicking the "Set Initial Point" button.</li>
    <li>Add or remove obstacles by clicking on the squares in the "Obstacle Editor" section.</li>
    <li>Watch the follower navigate the maze in real-time by clicking the "Simulation" button.</li>
  </ol>

  <h2>Credits</h2>
  <p>This app was created by Dinith Heshan as the final year project of my degree.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="https://github.com/DinithHeshan/q-learning-maze-follower-app/blob/master/LICENCE">LICENSE</a> file for details.</p>
</body>
</html>
