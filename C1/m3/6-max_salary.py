def max_salary(nums):
    nums = list(map(str, nums))
    result = []
    while nums:
        max_num = nums[0]
        for num in nums:
            if num + max_num > max_num + num:
                max_num = num
        result.append(max_num)
        nums.remove(max_num)
    return "".join(result)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    result = max_salary(nums)
    print(int(result))
