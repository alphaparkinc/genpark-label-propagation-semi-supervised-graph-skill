# genpark-label-propagation-semi-supervised-graph-skill

Agent Skill implementing the **Semi-Supervised Label Propagation Algorithm (LPA)** propagating sparse seed node annotations across complex graph topologies.

## Architectural Overview
```mermaid
flowchart TD
    Seeds["Seed Labeled Nodes (Clamped)"] & Graph["Graph Adjacency"] --> Step["Synchronous Neighborhood Inspection"]
    Step --> Tally["Tally Neighbor Label Multiset Counts"]
    Tally --> Majority["Adopt Argmax Frequent Neighbor Class"]
    Majority --> Converge{"Label Equivalence / Max Iterations ?"}
    Converge -- No --> Step
    Converge -- Yes --> Partition["Dense Graph Classification Partition"]
```
