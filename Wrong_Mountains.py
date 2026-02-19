def valid_mountain_array(hight_list) -> bool:
    start_index = 0
    if len(hight_list) <3:
        return False
    while start_index +1 < len(hight_list) and (hight_list[start_index] <
                                                hight_list[start_index + 1]):
        start_index += 1
    if start_index == 0 or start_index == len(hight_list) - 1:
        return False
    while start_index +1 < len(hight_list) and (hight_list[start_index] >
                                                hight_list[start_index + 1]):
            start_index += 1
    return start_index == len(hight_list) - 1

if __name__ == '__main__':
    try:
        
        berg_hight: list[int] = list(map(int, input().split()))
        
        print(valid_mountain_array(berg_hight))
    except EOFError:
        pass