q = int(input())

t = []


def odd_even_position(nums):
    
	return all(nums[i]%2==i%2 for i in range(1,len(nums)))
	
	
for i in range(0,q):
    m,n = input().split()
    m = int(m)
    n = int(n)
    count=0
    while(m<=n):
        digits = [int(x) for x in str(m)]
        digits.insert(0,0)
        answer = odd_even_position(digits)
        if(answer == True):
            count = count+1
        m += 1
    t.append(count)

for i in range(len(t)):
    print("Case #"+str(i+1)+": "+str(t[i]))