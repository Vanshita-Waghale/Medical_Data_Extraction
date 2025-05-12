def find_spillage(water_requirements, max_trips):
    def is_possible(capacity):
        trips_needed = 0
        spillage = 0

        for requirement  in water_requirements:
            trips_needed += (requirement + capacity - 1) // capacity

        spillage = max(0, (trips_needed - max_trips) * capacity)

        return spillage

    left, right = 1, max(water_requirements) * max_trips
    while left < right:
        mid = (left + right) // 2
        spillage = is_possible(mid)

        if is_possible(mid) <= is_possible(mid + 1):
            right = mid
        else:
            left = mid + 1

    return left, is_possible(left)
water_requirements = [4, 3, 5, 2, 1,7]
max_trips = 5
min_capacity, spillage = find_spillage(water_requirements, max_trips)
print("Minimum possible capacity of the tempo:", min_capacity)
print("Spillage:", spillage)
