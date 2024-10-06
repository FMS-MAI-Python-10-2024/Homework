def solve():
    nums = [int(num) for num in input().split()]
    k = int(input())
    nums.sort()
    ans = 1e10
    for i in range(len(nums) - k + 1):
        ans = min(ans, nums[i + k - 1] - nums[i])

    return ans