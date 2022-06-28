# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        sum_number = str(self.calculateSum(l1) + self.calculateSum(l2))

        last_list_node = None
        for number in sum_number:
            if last_list_node is None:
                last_list_node = ListNode(number)
            else:
                last_list_node = ListNode(number, last_list_node)

        return last_list_node

    def calculateSum(self, node, multiplier=1):
        if node == None:
            return 0
        else:
            return node.val * multiplier + self.calculateSum(node.next, multiplier*10)


"""
[2,4,3]
[5,6,4]
[0]
[0]
[9,9,9,9,9,9,9]
[9,9,9,9]
"""
