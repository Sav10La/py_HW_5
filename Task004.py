# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('Task004.txt', 'r', encoding = 'utf_8') as f:
    for line in f.readlines():
        print(line)

def compress(sequence):
    count = 1
    result = []
    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1
    result.append((sequence[len(sequence) - 1], count))
    return result

def recover(sequence):
    result = []
    for item in sequence:
        result.append(item[0] * item[1])
    return "".join(result)

def format_output(sequence):
    result = []
    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])
    return "".join(result)

c = compress(line)
r = recover(c)

print("Initial line: " + line)
print("Compressed line: " + format_output(c))
print("Recovered line: " + r)

# Compress text
f = open('Task004.txt','a', encoding = 'utf_8')
f.writelines(format_output(c) + '\n')
f.close()

# # Recover text
# f = open('Task004.txt','a', encoding = 'utf_8')
# f.writelines(r + '\n')
# f.close()