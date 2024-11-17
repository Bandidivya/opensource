def cal_difference(n, m, arr):
    num1 = sum(i for i in arr if i % m !=0)
    num2 = sum(i for i in arr if i % m== 0)
    return num2 - num1
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
print(cal_difference(n, m, arr))
