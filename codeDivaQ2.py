def getK(N,K):
    temp = N  
    s = 0
    while (K):  
        s= sum(map(int, str(temp)))
        if(s%5==0):
            K=K-1
            N=N+1
            temp=N
            if(K==0):
                print(N-1)
        else:
            N=N+1
            temp=N



def main():
    N=int(input())
    K=int(input())
    
    getK(N,K)
    

if __name__=="__main__":
    main()