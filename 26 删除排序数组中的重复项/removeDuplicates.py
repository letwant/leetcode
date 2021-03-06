data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    length = len(nums)
    nums.sort()
    index = 1
    # 通过正向遍历删除元素
    while index < length:
        if nums[index] == nums[index - 1]:
            nums.remove(nums[index - 1])
            length -= 1
            continue
        index += 1
    return len(nums)


def removeDuplicates1(nums):
    # 可以通过反向遍历的方法删除元素
    for num_index in range(len(nums) - 1, 0, -1):  # python的反向遍历
        if nums[num_index] == nums[num_index - 1]:
            nums.pop(num_index)
    return len(nums)


def removeDuplicates2(nums):
    # 通过双指针法去重，效率高，方法妙
    nums.sort()
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates1(data))

print(data)
