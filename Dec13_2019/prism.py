


def surface_area(a, b, c):

    return (2 * a * b) + (2 * a * c) + (2 * b * c)


def volume(a, b, c):

    return (a * b * c)


def main():

    MAX = 10000

    for a in range(1, MAX):
        for b in range(1, MAX):
            for c in range(1, MAX):
                vol = volume(a, b, c)
                surf = surface_area(a, b, c)

                if vol == surf:
                    print "{5}: {0} x {1} x {2}, vol = {3}. surf = {4}".format(a, b, c, vol, surf, vol == surf)



main ()
