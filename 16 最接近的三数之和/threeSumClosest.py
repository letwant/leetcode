def threeSumClosest(nums, target):
    ans = 0
    lens = len(nums)
    if lens < 3:
        return ans
    nums.sort()
    # ans = float("inf")  # 代表正无穷
    ans = nums[0] + nums[1] + nums[2]
    for i in range(lens):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        L = i + 1
        R = lens - 1
        while L < R:
            tmp_sum = nums[i] + nums[L] + nums[R]
            if tmp_sum == target:
                return target
            if abs(tmp_sum - target) < abs(ans - target):
                ans = tmp_sum
                # L += 1  # 加上这个出错
            elif tmp_sum - target < 0:
                L += 1
            else:
                R -= 1
    return ans


print(threeSumClosest([0, 2, 1, -3], 1))
