#!/usr/bin/env python
# @Time     : 2018/5/2 下午10:13
# @Author   : cancan
# @File     : question_10.py
# @Function : 有效的数独

"""
Question:
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
1.数字 1-9 在每一行只能出现一次。
2.数字 1-9 在每一列只能出现一次。
3.数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。

Example 1:
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

Example 2:
输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

Note:
1.一个有效的数独（部分已被填充）不一定是可解的。
2.只需要根据以上规则，验证已经填入的数字是否有效即可。
3.给定数独序列只包含数字 1-9 和字符 '.' 。
4.给定数独永远是 9x9 形式的。
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def f(temp, x, y):
            if board[x][y] != '.' and 0 < int(board[x][y]) < 10:
                if board[x][y] in temp:
                    return False
                else:
                    temp.append(board[x][y])
                    return True
            else:
                return True

        for x in range(9):
            t_x = []
            t_y = []
            for y in range(9):
                if not f(t_x, x, y):
                    return False
                if not f(t_y, y, x):
                    return False

        for start_x in [0, 3, 6]:
            for start_y in [0, 3, 6]:
                t = []
                for x in range(start_x, start_x + 3):
                    for y in range(start_y, start_y + 3):
                        if not f(t, x, y):
                            return False

        return True


if __name__ == "__main__":
    s = Solution()
    d = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "9", ".", ".", ".", ".", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "9", "9", "3", "5", "7", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "4", "."],
         [".", ".", ".", "8", ".", ".", ".", ".", "."],
         [".", "1", ".", ".", ".", ".", "4", ".", "9"],
         [".", ".", ".", "5", ".", "4", ".", ".", "."]]
    print(s.isValidSudoku(d))
