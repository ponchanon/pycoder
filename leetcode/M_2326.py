# Title: Spiral Matrix IV

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def update_matrix(x, y):
            nonlocal head
            if head:
                matrix[x][y] = head.val
                head = head.next

        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        left, right, top, bottom = 0, n - 1, 0, m - 1

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                update_matrix(top, i)
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                update_matrix(i, right)
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    update_matrix(bottom, i)
                bottom -= 1

            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    update_matrix(i, left)
                left += 1

        return matrix
