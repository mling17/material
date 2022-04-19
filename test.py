
"""
1. 字符串转成列表
2。 从列表的末尾开始往外弹出字符
3。 弹出字符组成一个新的字符串
4。 如果新字符串长度是4就加入到组中
5。 循环结束如果新字符串长度不等于0就加到组中
6。 返回分组
"""


def four_split(num):
    # 1. 字符串转成列表
    num = list(num)
    group = []
    # 2。 从列表的末尾开始往外弹出字符
    temp = ''
    for i in range(len(num)):
        # 3。 弹出字符组成一个新的字符串
        temp = num.pop() + temp
        if len(temp) == 4:
            # 4。 如果新字符串长度是4就加入到组中
            group.insert(0, temp)
            temp = ''
    # 5。 循环结束如果新字符串长度不等于0就加到组中
    if len(temp) != 0:
        group.insert(0, temp)
    # group.reverse()
    # 6。 返回分组
    return group


# ret = four_split(n)


dict_ref = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九', '0': '零'}
digit = ['十', '百', '千']

n = '987600021010'


# n = '9876543201'


def exchange(num):
    # 0。 去左侧的零
    num = num.lstrip('0')
    # 1. 先把数字转成汉字
    temp = []
    for i in num:
        temp.append(dict_ref[i])
    for j in range(len(temp) - 1):
        temp.insert(-(2 * j + 1), digit[j])
    ans = ''.join(temp)
    while '零千' in ans or '零百' in ans or '零十' in ans or '零零' in ans or '零零零' in ans:
        for i in ('零千', '零百', '零十', '零零', '零零零'):
            if i in ans:
                ans = ans.replace(i, '零')
    if ans[-1] == '零':
        return ans[:-1]
    return ans
    """"
    特殊情况
    1。 零千
    2。 零百
    3。 零十
    4。 零零
    5。 零零零
    6。 末尾是零
    """


# 1. 分组
num_split = four_split(n)
# 2。 根据分组创建数级列表
if len(num_split) == 3:
    units = ['亿', '万', '']
elif len(num_split) == 2:
    units = ['万', '']
else:
    units = ['']
# 3。 把数字和数级连接
ans = ''
for index, num in enumerate(num_split):
    ret = exchange(num)
    unit = units[index]
    ans = ans + ret + unit
print(ans)





# 杨辉三角

dict_ref = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九', '0': '零'}
digit = ['十', '百', '千']

n = '987600021010'


# n = '9876543201'


def exchange(num):
    # 0。 去左侧的零
    num = num.lstrip('0')
    # 1. 先把数字转成汉字
    temp = []
    for i in num:
        temp.append(dict_ref[i])
    for j in range(len(temp) - 1):
        temp.insert(-(2 * j + 1), digit[j])
    ans = ''.join(temp)
    while '零千' in ans or '零百' in ans or '零十' in ans or '零零' in ans or '零零零' in ans:
        for i in ('零千', '零百', '零十', '零零', '零零零'):
            if i in ans:
                ans = ans.replace(i, '零')
    if ans[-1] == '零':
        return ans[:-1]
    return ans
    """"
    特殊情况
    1。 零千
    2。 零百
    3。 零十
    4。 零零
    5。 零零零
    6。 末尾是零
    """


# 1. 分组
num_split = four_split(n)
# 2。 根据分组创建数级列表
if len(num_split) == 3:
    units = ['亿', '万', '']
elif len(num_split) == 2:
    units = ['万', '']
else:
    units = ['']
# 3。 把数字和数级连接
ans = ''
for index, num in enumerate(num_split):
    ret = exchange(num)
    unit = units[index]
    ans = ans + ret + unit
print(ans)
