#!/usr/bin/env python
# @Time     : 2018/7/15 下午1:49
# @Author   : cancan
# @File     : method_1.py
# @Function : 4的幂

"""
Question:
给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。

Example:
当 num = 16 时 ，返回 true 。 当 num = 5时，返回 false。

Follow up
你能不使用循环/递归来解决这个问题吗？

Credits:
特别感谢 @yukuairoy 添加这个问题并创建所有测试用例。
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while True:
            if num == 1:
                return True
            if num % 4 == 0:
                num = num // 4
            else:
                return False
