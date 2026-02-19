def is_correct_bracket_seq(seq: str) -> bool:
    stek = []
    word_def = {')': '(', ']': '[', '}': '{'}
    for char in seq:
        if char in ('([{'):
            stek.append(char)
        else:
            if not stek:
                return False
            last_open = stek.pop()
            if last_open != word_def[char]:
                return False
    return len(stek) == 0

if __name__ == '__main__':
    sequence = input().strip() 
    print(is_correct_bracket_seq(sequence))