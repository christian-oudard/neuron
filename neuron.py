# Write a programming language compiler targeting this simulation.
# Rewrite this simulation in that programming language.
# Redo in C for speed.


def simulate(graph, initial, max_t):
    size = len(graph)
    assert len(initial) == size

    state = list(initial)

    for t in range(max_t):
        yield state
        next_state = [0] * size
        for source, targets in graph.items():
            if state[source] == 1:
                for target in targets:
                    next_state[target] = 1
        state = next_state


def loop(n):
    d = {}
    for i in range(n):
        d[i] = [(i + 1) % n]
    return d
