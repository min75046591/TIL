"""
0보다 크고 1보다 작은 십진수 N을 이진수로 바꿔라
소수점 12자리 이내면 0. 을 제외한 뒤에만 출력
13자리 이상이 필요하면 'overflow' 출력

= 1 * 2 ** -1 + 0 * 2 ** -2 + 1 * 2 ** -3
= 0.5 + 0 + 0.125
= 0.625
"""
# def dec_float(float_num):
#     bin = ""
#     # 소수점 이하 최대 12자리 까지만 계산
#     while len(bin) <= 12:
#         float_num *= 2
#         s = str(float_num).split(".")
#         bin += s[0]
#
#         if len(bin) > 12:
#             print(f'#{tc} overflow')
#
#         if s[1] == "0":
#             return bin
#
#         float_num = float("0." + s[1])
#
#     return bin
# T = int(input())
# for tc in range(1, T+1):
#     float_num = float(input())
#     print(f'#{tc} {dec_float(float_num)}')

def dec_float(float_num: float) -> str:
    bin_str = ""
    # 소수점 이하 최대 12자리 까지만 계산
    while len(bin_str) < 14 or len(bin_str.split(".")[1]) > 12:
        float_num *= 2
        s = str(float_num).split(".")
        bin_str += s[0]

        if len(bin_str) - 2 > 12:
            print(f'#{tc} overflow')

        if s[1] == "0":
            return bin_str

        float_num = float("0." + s[1])

    return bin_str

T = int(input())
for tc in range(1, T+1):
    float_num = float(input())
    print(f'#{tc} {dec_float(float_num)}')

