def car_fueling(distance, tank_capacity, no_of_bunks, bunks):
    result = 0
    last_bunk = 0
    last_bunk_index = 0
    while distance > 0 and distance > tank_capacity:
        best_bunk = -1
        for i in range(last_bunk_index, no_of_bunks):
            if bunks[i] - last_bunk <= tank_capacity:
                best_bunk = i
            else:
                break
        if best_bunk == -1:
            return -1
        result += 1
        distance -= (bunks[best_bunk] - last_bunk)  # Correctly reduce the remaining distance
        last_bunk = bunks[best_bunk]
        last_bunk_index = best_bunk+1

    return result


if __name__ == "__main__":
    distance = int(input())
    tank_capacity = int(input())
    no_of_bunks = int(input())
    bunks = list(map(int, input().split()))

    print(car_fueling(distance, tank_capacity, no_of_bunks, bunks))
