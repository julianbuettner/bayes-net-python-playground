from typing import Dict, List, Set
from .node import Node, CPT


class BayesNet:
    def __init__(self, node_cpts: Dict[Node, CPT]):
        self.node_cpts = node_cpts

    def get_direct_parent_nodes(self, node: Node) -> List[Node]:
        return self.node_cpts[node].nodes

    def try_to_set_value_for_node(self, node: Node) -> bool:
        """False if calculation happeneds, true otherwise."""

        # Value is already calculated.
        if node.prob is not None:
            return True

        # Check if all parents have usable values
        for parent in self.get_direct_parent_nodes(node):
            if parent.prob is None:
                return True

        # Get parent values for calculation
        parent_values: List[float] = [
            p.prob for p in self.get_direct_parent_nodes(node)
        ]
        result = self.node_cpts[node].calc_probability(parent_values)
        node.prob = result
        return False

    def infere(self):
        counter = -1
        while counter != 0:
            counter = 0
            for node in self.node_cpts.keys():
                if not self.try_to_set_value_for_node(node):
                    counter += 1
            print("Inference run. Calculated nodes:", counter)
        print("Done")

    def print_nice(self):
        for node in self.node_cpts.keys():
            print("=" * len(node.name))
            print(node.name)
            self.node_cpts[node].print_nice()
            print()
