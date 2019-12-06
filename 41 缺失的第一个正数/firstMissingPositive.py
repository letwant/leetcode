def firstMissingPositive(nums: list) -> int:
    nums.sort()
    i = 1
    index = 1
    length = len(nums)
    if length == 1:
        if nums[0] != 1:
            return 1
        return 2
    while index < length:
        if nums[index] > 0:
            if i == nums[index]:
                if nums[index] == nums[index - 1]:
                    index += 2
                else:
                    index += 1
                i += 1
            else:
                return i
    return i


print(firstMissingPositive([1, 2, 0]))
