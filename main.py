# move
RIGHT_UP = 0
RIGHT_DOWN = 1
LEFT_UP = 2
LEFT_DOWN = 3
UP_RIGHT = 4
UP_LEFT = 5

option = ['right - down',
          'right - up',
          'left - down',
          'left - up',
          'up - left',
          'up - right']


def generate():
    print 'please input the cube:'
    target = raw_input()
    tree = get_tree(target)
    i = len(tree) - 1
    j = 1
    if tree:
        print 'number of options:', tree[-1][3]
        while tree[i][2] > -1:
            print j, option[tree[i][2]]
            i = tree[i][1]
            j += 1


def get_tree(target):
    tree = [("bbbbggggoooorrrryyyywwww", 0, -1, 0)]
    ind = 0
    while ind < 5000:
        c = tree[ind][0]
        for i in range(6):
            c_new = move_cube(c, i)
            if c_new not in zip(*tree)[0]:
                tree.append((c_new, ind, i, tree[ind][3] + 1))
                if c_new == target:
                    return tree
        ind += 1
    return None


def move_cube(c, move):
    if move == RIGHT_UP:
        m = [2, 0, 3, 1,
             4, 5, 6, 7,
             20, 9, 21, 11,
             16, 13, 17, 15,
             10, 8, 18, 19,
             14, 12, 22, 23]
    elif move == RIGHT_DOWN:
        m = [1, 3, 0, 2,
             4, 5, 6, 7,
             17, 9, 16, 11,
             21, 13, 20, 15,
             12, 14, 18, 19,
             8, 10, 22, 23]
    elif move == LEFT_UP:
        m = [20, 1, 22, 3,
             16, 5, 18, 7,
             10, 8, 11, 9,
             12, 13, 14, 15,
             2, 17, 0, 19,
             6, 21, 4, 23]
    elif move == LEFT_DOWN:
        m = [18, 1, 16, 3,
             22, 5, 20, 7,
             9, 11, 8, 10,
             12, 13, 14, 15,
             4, 17, 6, 19,
             0, 21, 2, 23]
    elif move == UP_RIGHT:
        m = [9, 8, 2, 3,
             13, 12, 6, 7,
             4, 5, 10, 11,
             0, 1, 14, 15,
             18, 16, 19, 17,
             20, 21, 22, 23]
    elif move == UP_LEFT:
        m = [12, 13, 2, 3,
             8, 9, 6, 7,
             1, 0, 10, 11,
             5, 4, 14, 15,
             17, 19, 16, 18,
             20, 21, 22, 23]
    else:
        m = range(24)
    new = []
    for i in range(24):
        new.append(c[m[i]])
    return ''.join(new)


generate()
