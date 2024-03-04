testcase = int(input())

index = 0
for k in range(testcase):
    num = int(input())

    # Store spaced items as a seperate element in List.
    List = list(map(int,input().strip().split()))
    
    # Store spaced items as a seperate element in values.
    values = list(map(int,input().strip().split()))
    XOR,Sum = values[0], values[1]
    for i in range(num):
        for j in range(i+1, num):
            # List[i],List[j] will pair up all posibilities.
            xor_value = List[i] ^ List[j]
            if (XOR== xor_value and Sum == (List[i]+List[j])):
                index += 1

print(index) # Gives back integer value.
