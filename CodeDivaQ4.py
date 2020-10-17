def getK(N,K):
    temp = int(N)
    i=0
    c=0
    s=0
    while(i<=temp):
        s = sum(map(int, str(i)))
        if(s%K==0):
            c=c+1
        i=i+1
    print(c)

def main():
    N=input()
    K=int(input())
    getK(N,K)

if __name__=="__main__":
    main()