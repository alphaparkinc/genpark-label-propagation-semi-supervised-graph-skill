"""Semi-Supervised Label Propagation Algorithm (LPA) Engine.
100% Python Standard Library.
"""

import collections

class LabelPropagationClassifier:
    """Semi-supervised Label Propagation Algorithm on graphs."""
    @staticmethod
    def propagate(adj_dict, initial_labels, max_iter=20):
        labels = dict(initial_labels)
        nodes = list(adj_dict.keys())

        for _ in range(max_iter):
            changed = False
            for u in nodes:
                if u in initial_labels:
                    continue
                nbrs = adj_dict[u]
                if not nbrs:
                    continue
                counts = collections.Counter()
                for v in nbrs:
                    if v in labels:
                        counts[labels[v]] += 1
                if counts:
                    most_common = counts.most_common(1)[0][0]
                    if labels.get(u) != most_common:
                        labels[u] = most_common
                        changed = True
            if not changed:
                break
        return labels
