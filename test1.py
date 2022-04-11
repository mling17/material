def triangle_2(n):
    """
    :param n: 需要生成的杨辉三角行数
    :return:
    """
    triangle = [1]  # 初始化杨辉三角
    for i in range(n):
        yield triangle
        triangle.append(0)  # 在最后一位加个0，用于计算下一行
        # triangle = [triangle[j] + triangle[j - 1] for j in range(len(triangle))]
        temp = []
        triangle = [1, 1, 0]
        for j in range(len(triangle)):
            temp.append(triangle[j] + triangle[j - 1])  # [1,1]
        triangle = temp


for i in triangle_2(10):
    print(i)
    # print(''.join(str(i)).center(50))  # 格式化输出
