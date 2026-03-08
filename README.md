# Uniform Cost Search (Artificial Intelligence)

This repository contains a Python implementation of the **Uniform Cost Search (UCS)** algorithm used to find the **optimal path in a weighted graph**.

## About the Algorithm

Uniform Cost Search is a search algorithm used in Artificial Intelligence to find the **lowest-cost path** from a start node to a goal node.
It expands nodes based on the **lowest cumulative path cost**.

UCS is similar to **Dijkstra's algorithm** and guarantees an **optimal solution** when all costs are positive.

## Features

* Graph input taken from the **user**
* Supports **weighted edges**
* Uses a **priority queue**
* Finds the **optimal path**
* Displays the **total cost**

## Requirements

* Python 3.x

## How to Run

Run the program using Python:

```
python uniform_cost_search.py
```

## Example Input

```
Enter number of nodes: 4
Enter node: A
Enter number of neighbors: 2
Enter neighbor node: B
Enter cost: 2
Enter neighbor node: C
Enter cost: 4
Enter node: B
Enter number of neighbors: 1
Enter neighbor node: D
Enter cost: 3
Enter node: C
Enter number of neighbors: 1
Enter neighbor node: D
Enter cost: 1
Enter node: D
Enter number of neighbors: 0
Enter start node: A
Enter goal node: D
```

## Example Output

```
Optimal Path: A -> C -> D
Total Cost: 5
```

## Author

Jagadeshwar Surneni
