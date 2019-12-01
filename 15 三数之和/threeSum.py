def threeSum(nums):
    num_len = len(nums)
    ans = []
    if num_len < 3:
        return ans
    nums.sort()
    for i in range(num_len):
        if nums[i] > 0:
            return ans
        if i > 0 and nums[i] == nums[i - 1]:  # nums[i] == nums[i-1]这个判断条件很经典
            continue
        L = i + 1
        R = num_len - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                ans.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L += 1
                while L < R and nums[R] == nums[R - 1]:
                    R -= 1
                L += 1
                R -= 1
            elif nums[i] + nums[L] + nums[R] > 0:
                R -= 1
            else:
                L += 1
    return ans


print(threeSum([0, 0, 0, 1, -3, 2]))
