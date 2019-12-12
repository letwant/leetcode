# 二分查找法,如果找到则返回索引,找不到返回-1
def binsearch(nums: list, target: int) -> int:
    length = len(nums)
    if length == 0:
        return -1
    left = 0
    right = length - 1
    mid = 0
    if nums[mid] == target:
        return mid
    while left < right:
        mid = int(right - left)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


print(binsearch([1, 2, 3, 7, 10, 11], 11))
