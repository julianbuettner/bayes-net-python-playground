from pybay import Node, CPT, BayesNet


def main():
    node_sprinkler = Node("Sprinkler")
    node_rain = Node("Rain")
    node_grass_wet = Node("Grass Wet")

    cpt_rain = CPT(
        [],  # No Parents
        [0.2],
    )
    cpt_sprinkler = CPT(
        [node_rain],
        [
            0.4,
            0.01,
        ],
    )
    cpt_grass_wet = CPT(
        [node_rain, node_sprinkler],
        [
            0.0,
            0.8,
            0.9,
            0.99,
        ],
    )
    bayesnet = BayesNet(
        {
            node_sprinkler: cpt_sprinkler,
            node_rain: cpt_rain,
            node_grass_wet: cpt_grass_wet,
        }
    )
    bayesnet.print_nice()
    node_rain.prob = 0.0
    bayesnet.infere()

    print("Value", node_grass_wet.prob)


main()
