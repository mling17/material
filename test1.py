# 输入层数n，打印n层杨辉三角
n = 5
triangle = []
for i in range(n):
    temp = []
    if i == 0:
        temp = [1]
    elif i == 1:
        temp = [1, 1]
    else:
        for j in range(i + 1):  # i=3, j = 0,1,2
            if j == 0 or j == i:
                temp.append(1)  # temp= [1,]
            else:
                temp.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(temp)
center = len(str(triangle[-1]).strip('[').strip(']').replace(',', '    '))
for i in triangle:
    i = str(i).strip('[').strip(']').replace(',', '    ')
    print(i.center(center))

