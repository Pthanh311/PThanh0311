# B1 tính chi so ROI(Return on Investment) chỉ số hoàn vốn sau khi đầu tư
def tinhRoi(doanhthu,chiphi):
    ROI=(doanhthu-chiphi)/chiphi
    if(ROI >=0.75):
        print("Có thể đầu tư")
    else:
        print("Không thể đầu tư do ROI <0.75")
# B2.1 ham tra ve gia tri cua day so Fibonacci tai vi tri n bat ky
def tinhFibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return tinhFibonacci(n-1)+tinhFibonacci(n-2)

'''
n=4
tinhFibonacci(4-1)+tinhFibonacci(4-2)
=tinhFibonacci(3)+tinhFibonacci(2)
=[tinhFibonacci(3-1)+tinhFibonacci(3-2)] + 1
=[tinhFibonacci(2)+tinhFibonacci(1)] + 1
=[1+1]+1
=3
'''
# B2.2 ham in ra day so cua Fibonacci tu 1-n
def daysoFibonacci(n):
    for i in range(1,n+1):
        print(tinhFibonacci(i),end="\t")
# bai 4
def oscillate(tu,den):
    list_oscillate=[]
    for i in range(tu,den):
        list_oscillate.append(i)
        list_oscillate.append(i*-1)
    return list_oscillate
'''
for n in oscillate(-3,5):
    print(n,end="\t")
tu=-3
den=5
list_oscillate=[]
oscillate(-3,5)
chay lan 1
i=-3=> list_oscillate[-3] => list_oscillate[-3,3]
chay lan 2 
i=i+1=> -3+1=-2 => list_oscillate[-3,3,-2,2]
.....
'''

# bai5 danh sach cac so ma n chi het (1->n-1)
def danhsachchiahet(n):
    list=[]
    for i in range(1,n):
        if(n%i==0):
            list.append(i)
    return list
def sohoanthien(n):
    tongsochiahet=sum(danhsachchiahet(n))
    if tongsochiahet==n:
        print("{0} la so hoan thien".format(n))
    if tongsochiahet >n:
        print("{0} la so thinh vuong".format(n))