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


def firstMissingPositive1(nums: list) -> int:
    length = len(nums)
    if length == 0:
        return 1
    for i in range(length):
        while nums[i] != i + 1:
            # 小心[1, 1]这种例子会造成死循环，要特殊处理。（nums[i] != nums[nums[i] - 1）
            if nums[i] <= 0 or nums[i] > length or nums[i] == nums[nums[i] - 1]:
                break
            tmp = nums[i] - 1
            nums[i] = nums[tmp]
            nums[tmp] = tmp + 1
    for i in range(length):
        if nums[i] != i + 1:
            return i + 1
    return length + 1


print(firstMissingPositive1([2, -1, 3, 5, 0, 2]))


def firstMissingPositive12(nums: list) -> int:
    length = len(nums)
    if length == 0:
        return 1
    for i in range(length):
        while 1 <= nums[i] <= length and i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
            tmp = nums[i] - 1
            nums[i] = nums[tmp]
            nums[tmp] = tmp + 1
    for i in range(length):
        if i != nums[i] - 1:
            return i + 1
    return length + 1


print(firstMissingPositive12([3, 4, -1, 1]))
