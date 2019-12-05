# 匹配子串使用最好使用KMP算法


# 暴力解法1，自己手写的，比较麻烦
def strStr1(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    i = 0
    while i < len(haystack):
        if needle[0] == haystack[i]:
            index = i
            for j in range(len(needle)):
                if needle[j] == haystack[index]:
                    index += 1
                    j += 1
                    if j == len(needle):
                        return i
                    if index == len(haystack):
                        return -1
                else:
                    i += 1
                    break
        else:
            i += 1
    if i == len(haystack):
        return -1


# 比较简洁的暴力遍历法，参考网上的思路
def strStr2(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    M, N = len(haystack), len(needle)
    for i in range(M - N + 1):  # N-M开始循环可以极大的缩短时间，正确的打开方式
        for j in range(N):
            if needle[j] != haystack[i + j]:
                break
            if j + 1 == N:
                return i
    return -1


print(strStr2(haystack="a", needle="a"))
