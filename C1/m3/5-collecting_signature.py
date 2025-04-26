def collecting_signature(segments):
    segments = sorted(segments, key=lambda x: x[1])

    points = []
    current_point = None

    for segment in segments:
        if current_point is None or segment[0] > current_point:
            current_point = segment[1]
            points.append(current_point)

    return len(points), points


if __name__ == "__main__":
    n = int(input())
    segments = [0] * n
    for i in range(n):
        segment = list(map(int, input().split()))
        segments[i] = segment
    len, points = collecting_signature(segments)
    print(len)
    print(points)
