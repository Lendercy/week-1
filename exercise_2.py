def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        lines.append((s[::-1]+s[1:]).center(4*size-3, "-"))

    for i in range(size-1, 0, -1):
        print(lines[i])
    for i in range(size):
        print(lines[i])
size = int(input("Enter the size of the rangoli: "))
# Sample usage:
print_rangoli(size)