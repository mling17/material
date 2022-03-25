with open('data_clean.txt', 'r',encoding='utf-8') as f:
    words = f.read().split('][')
    for i in words:
        print(i.strip('[]'))