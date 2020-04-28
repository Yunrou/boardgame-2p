import numpy as np

table4 = {
    (0, 0): 3, (0, 1): 5, (0, 2): 5, (0, 3): 3,
    (1, 0): 5, (1, 1): 8, (1, 2): 8, (1, 3): 5,
    (2, 0): 5, (2, 1): 8, (2, 2): 8, (2, 3): 5,
    (3, 0): 3, (3, 1): 5, (3, 2): 5, (3, 3): 3
}

table6 = {
    (0, 0): 3, (0, 1): 5, (0, 2): 5, (0, 3): 5, (0, 4): 5, (0, 5): 3,
    (1, 0): 5, (1, 1): 8, (1, 2): 8, (1, 3): 8, (1, 4): 8, (1, 5): 5,
    (2, 0): 5, (2, 1): 8, (2, 2): 8, (2, 3): 8, (2, 4): 8, (2, 5): 5,
    (3, 0): 5, (3, 1): 8, (3, 2): 8, (3, 3): 8, (3, 4): 8, (3, 5): 5,
    (4, 0): 5, (4, 1): 8, (4, 2): 8, (4, 3): 8, (4, 4): 8, (4, 5): 5,
    (5, 0): 3, (5, 1): 5, (5, 2): 5, (5, 3): 5, (5, 4): 5, (5, 5): 3
}

SUMindex = {
    (4, 0, 0): np.array([(0, 0), (0, 1), (1, 1), (1, 0)]),
    (4, 0, 1): np.array([(0, 1), (1, 2), (1, 1), (0, 0), (0, 2), (1, 0)]),
    (4, 0, 2): np.array([(0, 2), (0, 1), (1, 2), (0, 3), (1, 3), (1, 1)]),
    (4, 0, 3): np.array([(0, 3), (1, 2), (1, 3), (0, 2)]),
    (4, 1, 0): np.array([(1, 0), (0, 1), (2, 0), (2, 1), (1, 1), (0, 0)]),
    (4, 1, 1): np.array([(1, 1), (0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (0, 0), (0, 2), (1, 0)]),
    (4, 1, 2): np.array([(1, 2), (0, 1), (2, 1), (0, 3), (1, 3), (2, 2), (1, 1), (0, 2), (2, 3)]),
    (4, 1, 3): np.array([(1, 3), (1, 2), (0, 3), (2, 2), (0, 2), (2, 3)]),
    (4, 2, 0): np.array([(2, 0), (2, 1), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (4, 2, 1): np.array([(2, 1), (3, 2), (1, 2), (2, 0), (2, 2), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (4, 2, 2): np.array([(2, 2), (3, 2), (1, 2), (2, 1), (1, 3), (1, 1), (3, 3), (3, 1), (2, 3)]),
    (4, 2, 3): np.array([(2, 3), (3, 2), (1, 2), (1, 3), (2, 2), (3, 3)]),
    (4, 3, 0): np.array([(3, 0), (2, 0), (2, 1), (3, 1)]),
    (4, 3, 1): np.array([(3, 1), (3, 2), (2, 0), (2, 1), (2, 2), (3, 0)]),
    (4, 3, 2): np.array([(3, 2), (2, 1), (2, 2), (3, 3), (3, 1), (2, 3)]),
    (4, 3, 3): np.array([(3, 3), (3, 2), (2, 2), (2, 3)]),

    (6, 0, 0): np.array([(0, 0), (0, 1), (1, 1), (1, 0)]),
    (6, 0, 1): np.array([(0, 1), (1, 2), (1, 1), (0, 0), (0, 2), (1, 0)]),
    (6, 0, 2): np.array([(0, 2), (0, 1), (1, 2), (0, 3), (1, 3), (1, 1)]),
    (6, 0, 3): np.array([(0, 3), (1, 4), (1, 2), (1, 3), (0, 4), (0, 2)]),
    (6, 0, 4): np.array([(0, 4), (1, 4), (0, 5), (1, 5), (0, 3), (1, 3)]),
    (6, 0, 5): np.array([(0, 5), (1, 4), (1, 5), (0, 4)]),
    (6, 1, 0): np.array([(1, 0), (0, 1), (2, 0), (2, 1), (1, 1), (0, 0)]),
    (6, 1, 1): np.array([(1, 1), (0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (0, 0), (0, 2), (1, 0)]),
    (6, 1, 2): np.array([(1, 2), (0, 1), (2, 1), (0, 3), (1, 3), (2, 2), (1, 1), (0, 2), (2, 3)]),
    (6, 1, 3): np.array([(1, 3), (1, 4), (2, 4), (1, 2), (0, 3), (2, 2), (0, 4), (0, 2), (2, 3)]),
    (6, 1, 4): np.array([(1, 4), (0, 5), (2, 5), (1, 5), (0, 3), (1, 3), (0, 4), (2, 3), (2, 4)]),
    (6, 1, 5): np.array([(1, 5), (1, 4), (0, 5), (2, 5), (0, 4), (2, 4)]),
    (6, 2, 0): np.array([(2, 0), (2, 1), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (6, 2, 1): np.array([(2, 1), (3, 2), (1, 2), (2, 0), (2, 2), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (6, 2, 2): np.array([(2, 2), (3, 2), (1, 2), (2, 1), (1, 3), (1, 1), (3, 3), (3, 1), (2, 3)]),
    (6, 2, 3): np.array([(2, 3), (1, 4), (3, 2), (3, 4), (1, 2), (1, 3), (2, 2), (3, 3), (2, 4)]),
    (6, 2, 4): np.array([(2, 4), (1, 4), (3, 4), (2, 5), (1, 5), (1, 3), (3, 3), (3, 5), (2, 3)]),
    (6, 2, 5): np.array([(2, 5), (1, 4), (1, 5), (3, 5), (2, 4), (3, 4)]),
    (6, 3, 0): np.array([(3, 0), (2, 0), (2, 1), (4, 0), (4, 1), (3, 1)]),
    (6, 3, 1): np.array([(3, 1), (3, 2), (2, 0), (2, 1), (4, 0), (4, 1), (2, 2), (3, 0), (4, 2)]),
    (6, 3, 2): np.array([(3, 2), (2, 1), (4, 1), (2, 2), (3, 3), (4, 2), (4, 3), (3, 1), (2, 3)]),
    (6, 3, 3): np.array([(3, 3), (3, 4), (3, 2), (2, 2), (4, 2), (4, 4), (4, 3), (2, 3), (2, 4)]),
    (6, 3, 4): np.array([(3, 4), (2, 5), (4, 4), (3, 3), (4, 5), (3, 5), (4, 3), (2, 3), (2, 4)]),
    (6, 3, 5): np.array([(3, 5), (2, 5), (4, 4), (4, 5), (2, 4), (3, 4)]),
    (6, 4, 0): np.array([(4, 0), (4, 1), (5, 0), (5, 1), (3, 0), (3, 1)]),
    (6, 4, 1): np.array([(4, 1), (3, 2), (5, 2), (4, 0), (5, 0), (4, 2), (3, 0), (5, 1), (3, 1)]),
    (6, 4, 2): np.array([(4, 2), (3, 2), (5, 2), (5, 3), (4, 1), (3, 3), (5, 1), (4, 3), (3, 1)]),
    (6, 4, 3): np.array([(4, 3), (3, 2), (5, 2), (5, 3), (4, 2), (3, 3), (4, 4), (5, 4), (3, 4)]),
    (6, 4, 4): np.array([(4, 4), (5, 3), (5, 5), (3, 3), (4, 5), (5, 4), (3, 5), (4, 3), (3, 4)]),
    (6, 4, 5): np.array([(4, 5), (5, 5), (4, 4), (5, 4), (3, 5), (3, 4)]),
    (6, 5, 0): np.array([(5, 0), (4, 1), (4, 0), (5, 1)]),
    (6, 5, 1): np.array([(5, 1), (5, 2), (4, 1), (4, 0), (5, 0), (4, 2)]),
    (6, 5, 2): np.array([(5, 2), (5, 3), (4, 1), (4, 2), (5, 1), (4, 3)]),
    (6, 5, 3): np.array([(5, 3), (5, 2), (4, 2), (4, 4), (5, 4), (4, 3)]),
    (6, 5, 4): np.array([(5, 4), (5, 3), (5, 5), (4, 4), (4, 5), (4, 3)]),
    (6, 5, 5): np.array([(5, 5), (4, 4), (4, 5), (5, 4)])
}


Xindex = {
    (4, 0, 0): np.array([(0, 1), (1, 1), (1, 0)]),
    (4, 0, 1): np.array([(1, 2), (1, 1), (0, 0), (0, 2), (1, 0)]),
    (4, 0, 2): np.array([(0, 1), (1, 2), (0, 3), (1, 3), (1, 1)]),
    (4, 0, 3): np.array([(1, 2), (1, 3), (0, 2)]),
    (4, 1, 0): np.array([(0, 1), (2, 0), (2, 1), (1, 1), (0, 0)]),
    (4, 1, 1): np.array([(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (0, 0), (0, 2), (1, 0)]),
    (4, 1, 2): np.array([(0, 1), (2, 1), (0, 3), (1, 3), (2, 2), (1, 1), (0, 2), (2, 3)]),
    (4, 1, 3): np.array([(1, 2), (0, 3), (2, 2), (0, 2), (2, 3)]),
    (4, 2, 0): np.array([(2, 1), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (4, 2, 1): np.array([(3, 2), (1, 2), (2, 0), (2, 2), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (4, 2, 2): np.array([(3, 2), (1, 2), (2, 1), (1, 3), (1, 1), (3, 3), (3, 1), (2, 3)]),
    (4, 2, 3): np.array([(3, 2), (1, 2), (1, 3), (2, 2), (3, 3)]),
    (4, 3, 0): np.array([(2, 0), (2, 1), (3, 1)]),
    (4, 3, 1): np.array([(3, 2), (2, 0), (2, 1), (2, 2), (3, 0)]),
    (4, 3, 2): np.array([(2, 1), (2, 2), (3, 3), (3, 1), (2, 3)]),
    (4, 3, 3): np.array([(3, 2), (2, 2), (2, 3)]),

    (6, 0, 0): np.array([(0, 1), (1, 1), (1, 0)]),
    (6, 0, 1): np.array([(1, 2), (1, 1), (0, 0), (0, 2), (1, 0)]),
    (6, 0, 2): np.array([(0, 1), (1, 2), (0, 3), (1, 3), (1, 1)]),
    (6, 0, 3): np.array([(1, 4), (1, 2), (1, 3), (0, 4), (0, 2)]),
    (6, 0, 4): np.array([(1, 4), (0, 5), (1, 5), (0, 3), (1, 3)]),
    (6, 0, 5): np.array([(1, 4), (1, 5), (0, 4)]),
    (6, 1, 0): np.array([(0, 1), (2, 0), (2, 1), (1, 1), (0, 0)]),
    (6, 1, 1): np.array([(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (0, 0), (0, 2), (1, 0)]),
    (6, 1, 2): np.array([(0, 1), (2, 1), (0, 3), (1, 3), (2, 2), (1, 1), (0, 2), (2, 3)]),
    (6, 1, 3): np.array([(1, 4), (2, 4), (1, 2), (0, 3), (2, 2), (0, 4), (0, 2), (2, 3)]),
    (6, 1, 4): np.array([(0, 5), (2, 5), (1, 5), (0, 3), (1, 3), (0, 4), (2, 3), (2, 4)]),
    (6, 1, 5): np.array([(1, 4), (0, 5), (2, 5), (0, 4), (2, 4)]),
    (6, 2, 0): np.array([(2, 1), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (6, 2, 1): np.array([(3, 2), (1, 2), (2, 0), (2, 2), (1, 1), (3, 0), (3, 1), (1, 0)]),
    (6, 2, 2): np.array([(3, 2), (1, 2), (2, 1), (1, 3), (1, 1), (3, 3), (3, 1), (2, 3)]),
    (6, 2, 3): np.array([(1, 4), (3, 2), (3, 4), (1, 2), (1, 3), (2, 2), (3, 3), (2, 4)]),
    (6, 2, 4): np.array([(1, 4), (3, 4), (2, 5), (1, 5), (1, 3), (3, 3), (3, 5), (2, 3)]),
    (6, 2, 5): np.array([(1, 4), (1, 5), (3, 5), (2, 4), (3, 4)]),
    (6, 3, 0): np.array([(2, 0), (2, 1), (4, 0), (4, 1), (3, 1)]),
    (6, 3, 1): np.array([(3, 2), (2, 0), (2, 1), (4, 0), (4, 1), (2, 2), (3, 0), (4, 2)]),
    (6, 3, 2): np.array([(2, 1), (4, 1), (2, 2), (3, 3), (4, 2), (4, 3), (3, 1), (2, 3)]),
    (6, 3, 3): np.array([(3, 4), (3, 2), (2, 2), (4, 2), (4, 4), (4, 3), (2, 3), (2, 4)]),
    (6, 3, 4): np.array([(2, 5), (4, 4), (3, 3), (4, 5), (3, 5), (4, 3), (2, 3), (2, 4)]),
    (6, 3, 5): np.array([(2, 5), (4, 4), (4, 5), (2, 4), (3, 4)]),
    (6, 4, 0): np.array([(4, 1), (5, 0), (5, 1), (3, 0), (3, 1)]),
    (6, 4, 1): np.array([(3, 2), (5, 2), (4, 0), (5, 0), (4, 2), (3, 0), (5, 1), (3, 1)]),
    (6, 4, 2): np.array([(3, 2), (5, 2), (5, 3), (4, 1), (3, 3), (5, 1), (4, 3), (3, 1)]),
    (6, 4, 3): np.array([(3, 2), (5, 2), (5, 3), (4, 2), (3, 3), (4, 4), (5, 4), (3, 4)]),
    (6, 4, 4): np.array([(5, 3), (5, 5), (3, 3), (4, 5), (5, 4), (3, 5), (4, 3), (3, 4)]),
    (6, 4, 5): np.array([(5, 5), (4, 4), (5, 4), (3, 5), (3, 4)]),
    (6, 5, 0): np.array([(4, 1), (4, 0), (5, 1)]),
    (6, 5, 1): np.array([(5, 2), (4, 1), (4, 0), (5, 0), (4, 2)]),
    (6, 5, 2): np.array([(5, 3), (4, 1), (4, 2), (5, 1), (4, 3)]),
    (6, 5, 3): np.array([(5, 2), (4, 2), (4, 4), (5, 4), (4, 3)]),
    (6, 5, 4): np.array([(5, 3), (5, 5), (4, 4), (4, 5), (4, 3)]),
    (6, 5, 5): np.array([(4, 4), (4, 5), (5, 4)])
}
