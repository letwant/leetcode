def searchInsert(nums: list, target: int):
    length = len(nums)
    if length == 0:
        return 0
    for i in range(length):
        if target > nums[i]:
            pass
        else:
            return i
    return length


print(searchInsert([1, 3, 5, 6], 7))
