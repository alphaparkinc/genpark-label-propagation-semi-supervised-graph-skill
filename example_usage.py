from client import LabelPropagationClassifier

graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C", "E"],
    "E": ["D", "F"],
    "F": ["E"]
}
seeds = {"A": "Cluster-1", "F": "Cluster-2"}
predicted = LabelPropagationClassifier.propagate(graph, seeds)
print("Propagated Node Labels:", predicted)
