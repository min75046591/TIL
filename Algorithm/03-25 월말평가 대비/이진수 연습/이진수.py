import sys
sys.stdin = open("input.txt", "r")

# 16진수를 4자리 2진수로 변환

nums = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    result = ''

    for i in hex_num:
        for j in nums:
            if i == j:
                result += str(nums[j])

    print(f'#{tc} {result}')