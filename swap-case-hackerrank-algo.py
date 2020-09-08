def swap_case(s):
    c=list(s)
    for i in range(len(c)):
        if(c[i].islower()):
            c[i]=c[i].upper()
        elif(c[i].isupper()):
            c[i]=c[i].lower()
        else:
            pass
    s="".join(c)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)