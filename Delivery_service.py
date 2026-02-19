def min_platforms(weights: list[int], limit: int) -> int:
    """Вычисление минимального количества
    платформ для перевозки роботов"""
    weights = sorted(weights)
    platforms: int = 0
    left: int = 0
    right: int = len(weights) - 1
    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        platforms += 1
        right -= 1
    return platforms


if __name__ == '__main__':
    robots_weights = [int(x) for x in input().split()]
    max_limit: int = int(input())
    print(min_platforms(robots_weights, max_limit))
