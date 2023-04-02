def print_operation_table(op, row=6, column =6):
    table = []
    for i in range(1, row+1):
        table_row = []
        for j in range(1, column+1):
            print(op(i,j), end=(" " * (6 - len(str(op(i,j))))))
        print()

print_operation_table(lambda x, y: x*y)
print_operation_table(lambda x, y: x+y)
print_operation_table(lambda x, y: x**y)
print_operation_table(lambda x, y: y**x)

        