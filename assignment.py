def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    minimum = min(values)
    maximum = max(values)
    total = sum(values)

    stats_record = (minimum, maximum, total)
    return stats_record

def main():
    num_days = int(input("Enter the number of days: "))

    original = []

    for _ in range(num_days):
        visits = int(input("Enter the number of website visits: "))
        original.append(visits)

    updated = original[:]

    correct_index = int(input("Enter the index to correct: "))
    new_visits = int(input("Enter the new number of visits: "))

    replace_value(updated, correct_index, new_visits)

    target = int(input("Enter the number of visits to search for: "))

    first_index = find_first(updated, target)
    count_matches = updated.count(target)

    stats_record = summarize(updated)
    minimum, maximum, total = stats_record

    sorted_list = sorted(updated)

    print(f"Original: {original}")
    print(f"Updated: {updated}")
    print(f"Sorted: {sorted_list}")
    print(f"Minimum number of visits: {minimum}")
    print(f"Maximum number of visits: {maximum}")
    print(f"Total number of visits: {total}")

    if first_index != -1:
        print(f"First matching index: {first_index}")
    else:
        print("Target not found")

    print(f"Matching values: {count_matches}")

if __name__ == "__main__":
    main()
