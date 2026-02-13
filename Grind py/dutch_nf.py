def sort123(nums):
    count1 = nums.count(1)
    count2 = nums.count(2)
    count3 = nums.count(3)

    nums[:] = [1]*count1 + [2]*count2 + [3]*count3
    return nums