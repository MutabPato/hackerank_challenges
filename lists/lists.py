if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        try:
            instruction = input().split()
            func = instruction[0]
            
            if func == 'insert':
                index = int(instruction[1])
                value = int(instruction[2])
                result.insert(index, value)
            elif func == 'print':
                print(result)
            elif func == 'remove':
                value = int(instruction[1])
                result.remove(value)
            elif func == 'append':
                value = int(instruction[1])
                result.append(value)
            elif func == 'sort':
                result.sort()
            elif func == 'pop':
                result.pop()
            elif func == 'reverse':
                result.reverse()
            
        except EOFError:
            break