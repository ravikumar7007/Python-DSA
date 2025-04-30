# import random


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


def count_segments(segments, points):
    events = []
    results = [0] * len(points)

    for l, r in segments:
        events.append((l, 1))
        events.append((r, -1))

    for i, p in enumerate(points):
        events.append((p, 0, i))

    # events = quick_sort(events, 0, len(events) - 1)
    events.sort(key=lambda x: (x[0], x[1]))  # Sort by first element, then by second

    count = 0

    for event in events:
        if event[1] == 1:
            count += 1
        elif event[1] == -1:
            count -= 1
        else:
            results[event[2]] = count

    return results


if __name__ == "__main__":
    n, m = map(int, input().split())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    points = list(map(int, input().split()))
    print(*count_segments(segments, points))
