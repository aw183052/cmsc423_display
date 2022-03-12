import sys
import os
import random
import math

def initialize_centers(k, n, points):
    return random.sample(points, k)

def dist(p1, p2):
    total = 0.0
    for x in range(0, len(p1)):
        total += pow(p1[x] - p2[x], 2)

    return total

def find_closest(point, keys):
    closest = keys[0]
    val = dist(point, closest)
    for k in keys:
        if val > dist(point, k):
            closest = k
            val = dist(point, k)
    
    return closest

def cen_to_clu(centers, points):
    clusters = dict()

    for p in points:
        key = find_closest(p, centers)
        if key in clusters:
            clusters[key].append(p)
        else:
            clusters[key] = [p]

    return clusters


def clu_to_cen(n, clusters):
    new_centers = list()

    for v in clusters.values():
        total = [0.0 for i in range(n)]
        for p in v:
            for i in range(n):
                total[i] += p[i]
        total = [round(total[i] / len(v), 5) for i in range(n)]
        new_centers.append(tuple(total))

    return new_centers

def comp_points(n, l1, l2):
    for x in range(len(l1)):
        for y in range(n):
            if not math.isclose(l1[x][y], l2[x][y]):
                return False

    return True

def main():
    f = open("input", "r")
    if os.path.exists("output"):
        os.remove("output")
    out = open("output", "w")
    
    first_line = f.readline().rstrip().split(" ")
    k = int(first_line[0])
    n = int(first_line[1])
    points = []

    for line in f.readlines():
        points.append(tuple([float(x) for x in line.rstrip().split(" ")]))

    centers = initialize_centers(k, n, points)
    prev = []
    
    while True:
        prev = sorted(centers)
        clusters = cen_to_clu(centers, points)
        centers = clu_to_cen(n, clusters)

        if comp_points(n, prev, sorted(centers)):
            break

    for c in centers:
        out.write(" ".join(str(p) for p in c) + "\n")
    f.close()
    out.close()

if __name__ == "__main__":
    main()