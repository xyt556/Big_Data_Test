# -*- codeing =utf-8 -*-
# @Time : 2023/2/14$ 12:25
# Author : YantaoXI
# @File : generate_pascal_triangle.py
# @Software: PyCharm
def generate_pascal_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    return result

def print_pascal_triangle(n):
    triangle = generate_pascal_triangle(n)
    for row in triangle:
        print(' '.join(str(x) for x in row))

# 打印 6 行的杨辉三角形
print_pascal_triangle(10)
