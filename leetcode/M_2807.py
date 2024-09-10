# Title: Insert Greatest Common Divisors in Linked List

from typing import Optional
from math import gcd


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first, second = head, head.next
        while second:
            greatest_common_divisor = gcd(first.val, second.val)  # Use built-in gcd
            node = ListNode(greatest_common_divisor)
            node.next = second
            first.next = node
            first, second = second, second.next

        return head
