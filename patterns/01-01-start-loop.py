# 1 2 3 4 5
# for i in range()

# print(list(range(5, )))

# print(help(range))

# print(list(range(1, 5 + 1, 1)))


# for i in range(1, 6, 1):
#     print(i)

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)


# print("1\n2\n3")


# print("a b c" * 2)

# for i in range(1, 6):
#     print("*" * i)


def draw_triangle(pattern, n_lines):
    beg = 1
    for i in range(beg, n_lines + 1):
        print(pattern * i)


def main():
    pattern = input("Enter the pattern character: ")
    n_lines = int(input("Number of lines for triangle (always enter a number): "))
    draw_triangle(pattern, n_lines)


if __name__ == "__main__":
    main()
