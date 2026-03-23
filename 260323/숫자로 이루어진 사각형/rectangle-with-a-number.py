def print_number_square(n):
    current_num = 1
    
    for i in range(n):
        for j in range(n):
            print(current_num, end=' ')
            current_num += 1

            if current_num > 9:
                current_num = 1
        print()

n = int(input())
print_number_square(n)