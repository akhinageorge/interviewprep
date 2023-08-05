#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
def miniMaxSum(arr):
    arr.sort()  
    minimum_sum = sum(arr[:4])  
    maximum_sum = sum(arr[1:])  
    print(minimum_sum, maximum_sum)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in range(len(arr)):
        if arr[i]<0:
            neg=neg+1
        elif arr[i]>0:
            pos=pos+1
        elif arr[i]==0:
            zero=zero+1
    print(pos/n)
    print(neg/n)
    print(zero/n)
          
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
