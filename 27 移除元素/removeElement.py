def removeElement(nums, val):
    # python正确的倒序法
    for i in range(len(nums)-1, -1, -1):
        print(i)
        if nums[i] == val:
            nums.remove(nums[i])
    return len(nums)

data = [3, 3]
print(removeElement(data, 3))
print(data)