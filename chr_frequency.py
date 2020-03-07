def char_frequency(n,aText_):
    #变量n代表需要统计的字符个数，aText是被统计的文本
    frequency = {}
    aText = list(aText_)
    if n == 1:
        for i in range(len(aText)):
            frequency.setdefault(aText[i],aText.count(aText[i]))
        print(frequency)
    if n == 2:
        for i in range(len(aText)):
            for j in range(i+1,len(aText)):
                chr_2 = aText[i] + aText[j]
                frequency.setdefault(chr_2,aText.count(chr_2))
        print(frequency)
    if n == 3:
        for i in range(len(aText)):
            for j in range(i+1,len(aText)):
                for k in range(j+1,len(aText)):
                    chr_3 = aText[i] + aText[j] +aText[k]
                    frequency.setdefault(chr_3,aText.count(chr_3))
        print(frequency)
    if n == 4:
        for i in range(len(aText)):
            for j in range(i+1,len(aText)):
                for k in range(j+1,len(aText)):
                    for l in range(k+1,len(aText)):
                        chr_4 = aText[i] + aText[j] + aText[k] + aText[l]
                        frequency.setdefault(chr_4,aText.count(chr_4))
        print(frequency)
s = "我们还我们是真的"
a_list = tuple(s)
print(a_list)
char_frequency(1,"我们还我们是真的")