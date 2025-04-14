def read_single_digit(d):
    digit_kor = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return digit_kor[int(d)]

def read_number(n):
    s = str(n)
    if len(s) == 1:
        return read_single_digit(s[0])
    elif len(s) == 2:
        return read_single_digit(s[0]) + read_single_digit(s[1])
    elif len(s) == 3:
        return read_single_digit(s[0]) + read_single_digit(s[1]) + read_single_digit(s[2])

num = int(input("세 자리 정수 입력: "))
print(read_number(num))
