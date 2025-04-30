import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(points, left, right):
    min_dist = float("inf")
    for i in range(left, right - 1):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist


def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip) - 1):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist


def closest_pair(points, left, right):
    if right - left <= 3:
        return brute_force(points, left, right + 1)

    mid = (left + right) // 2
    mid_x = points[mid][0]

    d1 = closest_pair(points, left, mid)
    d2 = closest_pair(points, mid + 1, right)
    d = min(d1, d2)

    strip = []
    for i in range(left, right + 1):
        if abs(points[i][0] - mid_x) < d:
            strip.append(points[i])

    return min(d, strip_closest(strip, d))


def minimum_distance(points):
    n = len(points)
    points.sort(key=lambda x: x[0])  # Sort by x-coordinate
    return closest_pair(points, 0, n - 1)


if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    result = minimum_distance(points)
    print(f"{result:.4f}")
