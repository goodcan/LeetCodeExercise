#!/usr/bin/env python
# @Time     : 2018/7/28 下午2:08
# @Author   : cancan
# @File     : method_2.py
# @Function : 缺失数字

"""
Question:
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

Example 1:
输入: [3,0,1]
输出: 2

Example 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

Note:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (1 + len(nums)) // 2 - sum(nums)
