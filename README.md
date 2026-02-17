Multi-Objective QoS Routing Optimization using RL & Meta-Heuristics
This project focuses on finding the optimal path in a complex, 250-node network topology based on conflicting Quality of Service (QoS) metrics. The problem is addressed as an NP-Hard optimization challenge using Reinforcement Learning and Meta-Heuristic algorithms.

Project OverviewNetwork Model: 
250 nodes with an Erdős-Rényi G(n,p) distribution (P=0.4).
Optimization Metrics:
*Latency: Minimizing total link and processing delays.
*Reliability: Maximizing path stability using logarithmic cost functions.
*Resource Usage: Optimizing bandwidth efficiency (1 Gbps basis).
Methodology: Weighted Sum Method to balance QoS weights (Wdelay + Wreliability + Wresource = 1).

My Contributions & Responsibilities
In this 7 member team project, I took the lead in the following core areas:

1. Technical Development (Lead Developer)

Q-Learning Implementation: I architected the Reinforcement Learning environment, defining states (nodes), actions (neighbor selection), and complex reward functions based on the path's total cost.
Network Topology Generator: I developed the module responsible for generating the 250-node graph and ensuring connectivity between source (S) and destination (D) pairs.

Mathematical Modeling: I implemented the conversion of multiplicative reliability metrics into additive "Reliability Costs" to enable efficient optimization.

2. Project Management & Leadership
Team Coordination: Acted as the Project Coordinator, organizing team meetings, synchronizing tasks between 7 members, and managing the integration of different modules.

Documentation & Reporting: I authored the interim reports and the final technical documentation, ensuring all academic requirements and performance analysis benchmarks were met.

Release Management: Managed the final delivery process, including code commenting, README preparation, and the demo presentation.
