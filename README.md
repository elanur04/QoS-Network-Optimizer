# Multi-Objective QoS Routing Optimization using RL & Meta-Heuristics

This project finds the optimal path in a complex 250-node network topology based on
conflicting Quality of Service (QoS) metrics. The problem is treated as an NP-hard
optimization challenge and solved with Reinforcement Learning and meta-heuristic algorithms.

## Project Overview

- **Network model:** 250 nodes with an Erdős–Rényi G(n, p) distribution (p = 0.4)
- **Optimization metrics**
  - **Latency:** minimizing total link and processing delays
  - **Reliability:** maximizing path stability using logarithmic cost functions
  - **Resource usage:** optimizing bandwidth efficiency (1 Gbps basis)
- **Method:** Weighted Sum Method to balance QoS weights
  (W<sub>delay</sub> + W<sub>reliability</sub> + W<sub>resource</sub> = 1)

## Algorithms

| Algorithm | File |
|---|---|
| Q-Learning (Reinforcement Learning) | `q_agent.py`, `main_qlearning.py` |
| Genetic Algorithm | `GenetikAlgoritma.py` |
| Ant Colony Optimization | `aco_router.py`, `run_aco_console.py`, `run_aco_experiments.py` |
| Graph model & metric evaluation | `Graf_Model.py`, `Metric_Evaluation.py` |
| Benchmark & visualization | `benchmark`, `gorsellestirme.py` |
| Desktop GUI (PyQt6 + pyqtgraph) | `arayüzMain.py` |

## My Contributions & Responsibilities

In this 7-member team project, I led the following areas:

### 1. Technical Development (Lead Developer)

- **Q-Learning implementation:** Architected the RL environment, defining states (nodes),
  actions (neighbor selection) and reward functions based on the path's total cost.
- **Network topology generator:** Developed the module that generates the 250-node graph
  and ensures connectivity between source (S) and destination (D) pairs.
- **Mathematical modeling:** Converted multiplicative reliability metrics into additive
  "reliability costs" to enable efficient optimization.

### 2. Project Management & Leadership

- **Team coordination:** Acted as project coordinator, organizing meetings, synchronizing
  tasks between 7 members and managing the integration of modules.
- **Documentation & reporting:** Authored the interim reports and final technical
  documentation, ensuring academic requirements and performance benchmarks were met.
- **Release management:** Managed the final delivery, including code comments, README
  and the demo presentation.

## Getting Started

```bash
git clone https://github.com/elanur04/QoS-Network-Optimizer.git
cd QoS-Network-Optimizer
pip install -r requirements.txt

python main_qlearning.py      # Q-Learning from the console
python run_aco_console.py     # Ant Colony Optimization from the console
python arayüzMain.py          # Desktop GUI comparing all algorithms
```

Node, edge and demand data come from the `BSM307_317_Guz2025_TermProject_*.csv` files.

## Input validation and tests

Console QoS weights must be finite, non-negative and include at least one positive value. Invalid input uses the documented default weights instead of dividing by zero.

```bash
python -m unittest discover -p "test_*.py"
```

The automated tests cover weight validation. They do not benchmark routing performance or establish an optimality guarantee for the heuristics.
