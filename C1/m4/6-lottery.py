import random


# def quick_sort(arr, low, high):
#     if len(arr) <= 1:
#         return arr
#     pi = random.randint(low, high)
#     less = [el for el in arr if el[0] < arr[pi][0]]
#     equal = [el for el in arr if el[0] == arr[pi][0]]
#     more = [el for el in arr if el[0] > arr[pi][0]]
#     return (
#         quick_sort(less, 0, len(less) - 1) + equal + quick_sort(more, 0, len(more) - 1)
#     )


from itertools import count


def count_segments(segments, points):
    events = []
    results = [0] * len(points)

    # Add segment start and end events
    for l, r in segments:
        events.append((l, -1))  # Start of a segment
        events.append((r, 1))  # End of a segment

    # Add point events with their original index
    for i, p in enumerate(points):
        events.append((p, 0, i))  # Point event

    # Sort events by x-coordinate, then by type (1 > 0 > -1)
    events.sort(key=lambda x: (x[0], x[1]))

    count = 0

    # Process events
    for event in events:
        if event[1] == -1:  # Start of a segment
            count += 1
        elif event[1] == 1:  # End of a segment
            count -= 1
        else:  # Point event
            results[event[2]] = count

    return results


def brute_force_count_segments(segments, points):
    results = []
    for point in points:
        count = 0
        for l, r in segments:
            if l <= point <= r:
                count += 1
        results.append(count)
    return results


def generate_random_segments_and_points(num_segments, num_points, coord_range):
    segments = [
        (
            random.randint(-coord_range, coord_range),
            random.randint(-coord_range, coord_range),
        )
        for _ in range(num_segments)
    ]
    segments = [
        (min(l, r), max(l, r)) for l, r in segments
    ]  # Ensure segments are ordered
    points = [random.randint(-coord_range, coord_range) for _ in range(num_points)]
    return segments, points


if __name__ == "__main__":
    n, m = map(int, input().split())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    points = list(map(int, input().split()))
    result = count_segments(segments, points)
    print(*result)

    # @Testing @ravikumar7007
    # while True:
    #     num_segments = 100
    #     num_points = 100
    #     coord_range = 100
    #     segments, points = generate_random_segments_and_points(
    #         num_segments, num_points, coord_range
    #     )

    #     print("Segments:", segments)
    #     print("Points:", points)

    #     # Optimized result
    #     optimized_result = count_segments(segments, points)

    #     # Brute force result
    #     brute_force_result = brute_force_count_segments(segments, points)

    #     # Compare results
    #     assert optimized_result == brute_force_result, (
    #         "Mismatch in results! Optimized: {}, Brute Force: {}".format(
    #             optimized_result, brute_force_result
    #         )
    #     )
