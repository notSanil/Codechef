n, m = list(map(int, input().split()))
grid = []
solution = []
for i in range(n):
    solution.append([])
    for j in range(m):
        solution[i].append(None)
for i in range(n):
    grid.append(list(input()))

w = int(input())
words = []
for i in range(w):
    words.append(input())

for j in range(n):
    for i in range(m):
        curr = grid[j][i]
        if curr == '#':
            solution[j][i] = '#'
        elif curr == '.':
            continue
        elif curr == 'r':
            k = i + 1
            while (grid[j][k] != 'r') and (grid[j][k] != 'b'):
                k += 1

            length = k - i + 1
            for word in words:
                if len(word) == length:
                    words.remove(word)
                    for l in range(i, k + 1):
                        if solution[j][l] is None or solution[j][l] == word[l - i]:
                            solution[j][l] = word[l - i]
                        else:
                            print('Invalid')
                            exit()
                    if grid[j][k] == 'b':
                        grid[j][k] = 'c'
                    else:
                        grid[j][k] = 'v1'
                    break
            else:
                print('Invalid')
                exit()

        elif curr == 'c':
            k = j + 1
            while grid[k][i] != 'c' and grid[k][i] != 'b':
                k += 1
            length = k - j + 1
            for word in words:
                if len(word) == length:
                    words.remove(word)
                    for l in range(j, k+1):
                        if solution[l][i] is None or solution[l][i] == word[l-j]:
                            solution[l][i] = word[l-j]
                        else:
                            print("Invalid")
                            exit()
                    if grid[k][i] == 'b':
                        grid[k][i] = 'r'
                    else:
                        grid[k][i] = 'v2'
                    break
            else:
                print("Invalid")
                exit()
        elif curr == 'b':
            x = i + 1
            while grid[j][x] != 'b' and grid[j][x] != 'r':
                x += 1
            lengthx = x - i + 1
            for word in words:
                if len(word) == lengthx:
                    words.remove(word)
                    for lx in range(i, x + 1):
                        if solution[j][lx] is None or solution[j][lx] == word[lx-i]:
                            solution[j][lx] = word[lx-i]
                        else:
                            print("Invalid")
                            exit()
                    if grid[j][x] == 'b':
                        grid[j][x] = 'c'
                    else:
                        grid[j][x] = 'v3'
                    break
            else:
                print("Invalid")
                exit()
            y = j + 1
            while grid[y][i] != 'b' and grid[y][i] != 'c':
                y += 1
            lengthy = y - j + 1
            for word in words:
                if len(word) == lengthy:
                    words.remove(word)
                    for ly in range(j, y+1):
                        if solution[ly][i] is None or solution[ly][i] == word[ly-j]:
                            solution[ly][i] = word[ly-j]
                        else:
                            print("Invalid")
                            exit()
                    if grid[y][i] == 'b':
                        grid[y][i] = 'r'
                    else:
                        grid[y][i] = 'v4'
                    break
            else:
                print("Invalid")
                exit()

for j in range(n):
    for i in range(m):
        print(solution[j][i], end='')
    print()
