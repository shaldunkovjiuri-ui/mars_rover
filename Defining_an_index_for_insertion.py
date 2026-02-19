def main():
    line = input().split()
    if not line:
        return
    nums = list(map(int, line))
    target = int(input())

    left = 0
    right = len(nums) - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if result != -1:
        print(result)
    else:
        print(left)
    
if __name__ == '__main__':
    main()
                 