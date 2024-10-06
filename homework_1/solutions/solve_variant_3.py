def solve():
    nums = [int(num) for num in input().split()]
    math_summ = (len(nums) * (len(nums) + 1)) // 2

    return (math_summ - sum(nums))
