"""
3-->三
2--》二
0--》零
字典
"""
import random

dict_ref = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九', '0': '零'}


# 列表插入  insert
def exchange(num):
    level = ['十', '百', '千']
    temp = []
    for i in num:
        temp.append(dict_ref[i])
    for j in range(len(temp) - 1):
        temp.insert(-(2 * j + 1), level[j])
    ans = ''.join(temp)
    for i in ['零十', '零百', '零千', '零零', '零零零']:
        if i in ans:
            ans = ans.replace(i, '零')
    ans = ans.rstrip('零')
    return ans
    """
        ['三', '二', '零', '一']
    0   -1   0      ['三', '二', '零', '十','一']
    1   -3   1      ['三', '二','百'， '零', '十','一']
    2   -5   2
    x   -(x*2+1)    j
    """


# ret = exchange(n)
# print(ret)
def four_split(num):
    num_list = list(num)
    temp = ''
    group = []
    for i in range(len(num_list)):
        temp = num_list.pop() + temp
        if len(temp) == 4:
            group.insert(0, temp)
            temp = ''
    if temp != '':
        group.insert(0, temp)
    return group


x = 0
while x < 10:
    n = str(random.randint(1, 99999999))
    print(f'{x}---->', n, end='\t')
    num_split = four_split(n)
    ans = ''
    for index, i in enumerate(num_split):
        if len(num_split) == 3:
            list_ref = ['亿', '万', '']
        elif len(num_split) == 2:
            list_ref = ['万', '']
        else:
            list_ref = ['']
        num = exchange(i)
        unit = list_ref[index]
        ans = ans + num + unit
    print(ans)
    x += 1

"""
1. 千位转换：
    -  将数字转成汉字，并转转成一个列表
    - 在相应的位置插入数位，千百十，
    - 含有['零十', '零百', '零千', '零零', '零零零']的情况替换成零
    - 末尾有零的情况要去掉零
2。 分组
    - 把数字转成列表
    - 在循环，从末尾开始pop组成一个新的字符串（四个长度）
    - 新的字符串插入都组

3。 各组转换完成后加入数级

课堂Bugs：
    1。 exchange函数，没有处理读数末尾是零的情况，应当使用rstrip将右侧的零去掉
    2。 four_split函数，当所有分组都是四位的时候，在for循环外应该判断temp是否是''，当是''时候不应该加入到group里
    3。 当分组只有一组的时候，应该加上else:list_ref = ['']
"""
