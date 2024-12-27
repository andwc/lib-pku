def max_submatrix(matrix):
    def kadane(arr):
        max_end_here=max_so_far=0
        for x in arr[1:]:
            max_end_here=max(max_end_here+x,x)
            max_so_far=max(max_so_far,max_end_here)
        return max_so_far
    rows=len(matrix)
    cols=len(matrix[0])
    max_sum=float('-inf')
    for left in range(cols):
        temp=[0]*rows
        for right in range(left,cols):
            for row in range(rows):
                temp[row]+=matrix[row][right]
            max_sum=max(max_sum,kadane(temp))
    return max_sum
n=int(input())
nums=[]
while len(nums)<n*n:
    nums.extend(input().split())
print(nums)
matrix=[list(map(int,nums[i*n:(i+1)*n])) for i in range(n)]
max_sum=max_submatrix(matrix)
print(max_sum)