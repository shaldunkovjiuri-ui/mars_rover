def main():
    n = int(input())
    nums = list(map(int, input().split()))
    write_index = 1
    
    for read_index in range(1, n):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index +=1
    result = nums[:write_index] + ['_'] * (n - write_index)
    print(*result)
main()