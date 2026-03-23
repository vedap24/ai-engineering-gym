# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None        # Starting lo previous emi undadu
        current = head     # Head nunchi start chestham
        
        while current is not None:
            # 1. Mundu unna train bogey ni temp lo hold cheyali
            temp = current.next
            
            # 2. Arrow ni venakki (prev vaipu) thippali
            current.next = prev
            
            # 3. Pointers ni okkadu munduku jarupali
            prev = current
            current = temp
            
        # Loop aipoyaka 'prev' kotha head aipotundi
        return prev

# Testing the code (Helper function to print list)
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 -> None
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("Original List:")
print_list(node1)

solution = Solution()
new_head = solution.reverseList(node1)

print("\nReversed List:")
print_list(new_head)