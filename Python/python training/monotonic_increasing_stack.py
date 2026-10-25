def monotonic_increasing_stack(arr):
    stack=[]
    for num in arr:
        while stack and stack[-1]>num:
            stack.pop()
        stack.append(num)
    return stack
arr=[8,7,9,3,2,4]
print(monotonic_increasing_stack(arr))

# output:[2, 4]