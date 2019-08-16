'''
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

Rectangle Area

示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
'''
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C-A)*(D-B)+(H-F)*(G-E) - max(0,min(C-E,G-A,G-E,C-A))*max(0,min(H-F,D-B,H-B,D-F))
        