def nukle(data: list[int]) -> list[int]:
    result = []
    count = 0
    for i in data:
        count = 0
        for n in data:
            if n < i:
                count += 1
        result.append(count)
    return result

if __name__ == '__main__':
    radiation_data = [int(x) for x in input().split()]
    final_result = nukle(radiation_data)
    print(*final_result)