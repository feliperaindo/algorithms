def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    dict_of_nums = {}

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False

        if num in dict_of_nums:
            return num
        dict_of_nums[num] = 1
    return False
