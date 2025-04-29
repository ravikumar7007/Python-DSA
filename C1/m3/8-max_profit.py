def minimal_moves_to_sit_together(positions):
    positions.sort()  # Sort the positions of friends
    median = positions[len(positions) // 2]
    post=[0] * len(positions)  # Find the median position
    for i, pos in enumerate(positions):
        post[i]=abs(pos - (median + i - len(positions) // 2))
    result = sum(post)
    return result

positions = [1, 3, 6]
result = minimal_moves_to_sit_together(positions)
print(result)  # Output: 2


















def min_switches_to_turn_on_bulbs(bulbs):
    switches = 0
    current_state = 0  # Tracks the current state of the bulbs (0 = off, 1 = on)

    for bulb in bulbs:
        # If the current bulb's state doesn't match the current state, press the switch
        if bulb != current_state:
            switches += 1
            current_state = 1 - current_state  # Flip the state (0 -> 1 or 1 -> 0)

    return switches

# bulbs = [0, 1, 0, 1]
# result = min_switches_to_turn_on_bulbs(bulbs)
# print(result)  # Output: 2










def connect_ropes_min_cost(ropes):
    ropes.sort()
    total_cost = 0

    while len(ropes) > 1:
        # Take the two smallest ropes
        first = ropes.pop(0)
        second = ropes.pop(0)

        # Connect them and calculate the cost
        cost = first + second
        total_cost += cost

        # Add the new rope back to the list
        ropes.append(cost)
        ropes.sort()

    return total_cost


# ropes = [4, 3, 2, 6]
# result = connect_ropes_min_cost(ropes)
# print(result)  # Output: 29


def can_cook_all_dishes(cook_times, fresh_times):
    dishes = sorted(
        zip(cook_times, fresh_times), key=lambda x: x[1]
    )  # Sort by freshness time
    total_cooking_time = 0

    for cook_time, fresh_time in dishes:
        total_cooking_time += cook_time
        if total_cooking_time > fresh_time:
            return False  # If the total cooking time exceeds the freshness time, it's not possible

    return True


# cook_times = [3, 2, 1]
# fresh_times = [5, 4, 3]
# result = can_cook_all_dishes(cook_times, fresh_times)
# print(result)  # Output: True


def max_independent_set(tree, n):
    visited = [False] * n
    result = []

    def dfs(node, parent_invited):
        if visited[node]:
            return
        visited[node] = True

        # If the parent is not invited, invite the current node
        if not parent_invited:
            result.append(node)
            for child in tree[node]:
                dfs(child, True)
        else:
            for child in tree[node]:
                dfs(child, False)

    dfs(0, False)
    return result


# n = 5
# tree = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0],
#     3: [1],
#     4: [1]
# }
# result = max_independent_set(tree, n)


def minimize_max_distance(mice, holes):
    mice.sort()
    holes.sort()
    distances = [
        abs(m - h) for m, h in zip(mice, holes)
    ]  # Calculate distances for debugging
    return max(distances)


# mice = [4, 2, 7]
# holes = [1, 5, 8]
# result = minimize_max_distance(mice, holes)
# print(result)  # Output: 3


def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[0] for job in jobs)

    # Create a schedule array to track job slots
    schedule = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        deadline, profit = job
        # Try to schedule the job at the latest available slot before its deadline
        for slot in range(deadline - 1, -1, -1):
            if schedule[slot] == -1:
                schedule[slot] = profit
                total_profit += profit
                break

    return total_profit, [profit for profit in schedule if profit != -1]


# jobs = [(2, 100), (1, 50), (2, 10)]
# total_profit, scheduled_jobs = job_scheduling(jobs)
# print(total_profit)  # Output: 150
# print(scheduled_jobs)  # Output: [50, 100]
