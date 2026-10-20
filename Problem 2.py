def smallest_number(numbers, target):
    if 0 > target:
        return 0

    #Taking the largest values first reaches the target with the fewest items.
    ordered = sorted(numbers, reverse=True)
    total = 0
    for count, value in enumerate(ordered, start=1):
        total += value
        if total > target:
            return count

    raise ValueError("No selection has a sum greater than the target.")


def main():
    n = int(input())
    target = int(input())
    numbers = list(map(int, input().split()))
    if len(numbers) != n:
        raise ValueError("The number of values must equal n.")

    answer = smallest_number(numbers, target)
    array_text = ",".join(str(value) for value in numbers)
    print(f"Input: {array_text} Target: {target} Answer: {answer}")


if __name__ == "__main__":
    main()
