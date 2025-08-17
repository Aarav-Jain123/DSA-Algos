def euclidean_algorithm__for_gcd_v1(a, b):
    if a == b:
        return a
    elif a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    elif a != 0 and b != 0:
        g = [a, b]
        while True:
            if g[0] > g[1]:
                g[0], g[1] = g[1], g[0]

            g[1] = g[1] - g[0]
            print(g)
            if g[0] == 0:
                print(g[1])
                break
            if g[1] == 0:
                print(g[0])
                break


# f = euclidean_algorithm__for_gcd_v1(192393289, 293287230)
# print(f)


def euclidean_algorithm__for_gcd_v2(a, b):
    if a == b:
        return a
    elif a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    elif a != 0 and b != 0:
        g = [a, b]
        if g[0] > g[1]:
            g[0], g[1] = g[1], g[0]
        q = g[1]/g[0]
        if q == 0:
            print(g[0])
        r = b%a
        print(r)
        g[1] = g[1] - r
        euclidean_algorithm__for_gcd_v1(g[0], g[1])


# f = euclidean_algorithm__for_gcd_v2(5, 1016)
# print(f)
def euclidean_algorithm__for_gcd_v3(a, b):
    if a == b:
        return a
    elif a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    elif a != 0 and b != 0:
        g = [a, b]
        if g[0] > g[1]:
            g[0], g[1] = g[1], g[0]
        q = g[1] / g[0]
        if q == 0:
            print(g[0])
        else:
            while True:
                r = g[1] % g[0]
                g[1] = g[0]*q + r
                g[0], g[1] = r, g[0]
                return  g[1]


# f = euclidean_algorithm__for_gcd_v3(5, 1016)
# print(f)