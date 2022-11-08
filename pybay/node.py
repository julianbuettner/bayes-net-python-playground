from typing import List, Optional, Tuple


def int_to_binary(value: int, size: int) -> List[int]:
    result = []
    for _ in range(size):
        if value & 1 == 1:
            result.append(1)
        else:
            result.append(0)
        value = value >> 1
    return list(reversed(result))


assert int_to_binary(7, 4) == [0, 1, 1, 1]
assert int_to_binary(8 + 2 + 1, 4) == [1, 0, 1, 1]


class Node:
    def __init__(self, name: str):
        self.name = name
        self._value = None

    @property
    def prob(self) -> Optional[float]:
        return self._value

    @prob.setter
    def prob(self, value):
        self._value = value

    def __str__(self):
        prob = None
        if self.prob is not None:
            prob = "{:.2f}".format(self.prob)
        return "{} [{}]".format(self.name, prob)


class CPT:
    def __init__(self, nodes: List[Node], table: List[float]):
        assert len(table) == 2 ** len(
            nodes
        ), "Table length: {}, node length: {}".format(len(table), len(nodes))
        self.nodes = nodes
        self.table = table

    def print_nice(self):
        for i in range(2 ** len(self.nodes)):
            flip_bool_arr = int_to_binary(i, len(self.nodes))
            pref = []
            for n in range(len(self.nodes)):
                pref.append(
                    "{:<8} = {}".format(self.nodes[n].name[:8], flip_bool_arr[n])
                )
            print(
                "{}   #  {:.3f} {:.3f}".format(
                    " | ".join(pref), self.table[i], 1 - self.table[i]
                )
            )

    def calc_probability(self, node_values: List[float], verbose=False):
        assert len(node_values) == len(self.nodes)
        prob = 0
        for i in range(2 ** len(node_values)):
            flip_bool_arr = int_to_binary(i, len(self.nodes))
            if verbose:
                print("i={}, bool table: {}".format(i, flip_bool_arr))
            # Prob of all priors (not)
            # fac = P(A=1) * P(B=1) * P(C=0)
            fac = 1
            for j in range(len(self.nodes)):
                if flip_bool_arr[j]:
                    fac *= node_values[j]
                else:
                    fac *= 1 - node_values[j]
            if verbose:
                print("\tprob += fac * self.table[i] =", fac, "*", self.table[i])

            # P(X=1 | A=1, B=1, C=0)
            prob += self.table[i] * fac
        return prob
