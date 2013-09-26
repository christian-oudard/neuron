from nose.tools import assert_equal

from neuron import simulate, loop


def test_loop():
    assert_equal(
        loop(1),
        {0: [0]}
    )
    assert_equal(
        loop(2),
        {0: [1], 1: [0]}
    )
    assert_equal(
        loop(3),
        {0: [1], 1: [2], 2: [0]}
    )


def test_simulate_simple():
    result = list(simulate(
        loop(1),
        [1],
        3,
    ))
    assert_equal(
        result,
        [
            [1],
            [1],
            [1],
        ]
    )

    result = list(simulate(
        {0: [0, 0]},
        [1],
        3,
    ))
    assert_equal(
        result,
        [
            [1],
            [1],
            [1],
        ]
    )

    result = list(simulate(
        loop(2),
        [1, 0],
        4,
    ))
    assert_equal(
        result,
        [
            [1, 0],
            [0, 1],
            [1, 0],
            [0, 1],
        ]
    )

    result = list(simulate(
        loop(3),
        [1, 0, 0],
        3,
    ))
    assert_equal(
        result,
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )

    result = list(simulate(
        loop(3),
        [1, 1, 0],
        3,
    ))
    assert_equal(
        result,
        [
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 1],
        ]
    )

    graph = {
        0: [1],
        1: [2],
        2: [0, 1],
    }
    result = list(simulate(
        graph,
        [1, 0, 0],
        8,
    ))
    assert_equal(
        result,
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
    )

    #result = list(simulate(
        #graph,
        #initial,
        #time,
    #))
    #assert_equal(
        #result,
        #[
        #]
    #)
