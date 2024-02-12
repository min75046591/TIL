for tc in range(1, 11):
    N, nums = input().split()
    stack = []

    for i in nums:
        if stack == []:
            stack.append(i)
            
        else:   
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    
    
    print(f'#{tc}',''.join(stack))
