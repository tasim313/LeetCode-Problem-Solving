'''given two non-empty linked lists, where each node contains a single digit. These digits are stored in reverse order, which means the 1s place is at the head of the list.

For example, the number 342 is stored as:

List: [2, 4, 3] -> means 2 + 40 + 300 = 342

also given another number in the same format, and asked to add these two numbers and return the result as a new linked list, also in reverse order.

Goal (What Needs to Be Solved)

We need to:

1. Traverse both linked lists.

2. Add corresponding digits together, just like doing elementary addition.

3. Handle carry-over when the sum of two digits is ≥ 10.

4. Return a new linked list that represents the sum, still in reverse order.


How to Analyze This Problem
🔸 Input:
    l1: A linked list representing the first number.

    l2: A linked list representing the second number.

🔸 Output:
    A linked list representing the sum of the two numbers, in reversed digit format.

🔸 Constraints:
    Each list has 1 to 100 nodes.

Each node has a digit 0–9.

We are not allowed to reverse the input lists or convert them to integers directly.


Example to Understand It Better

Example:

Input: l1 = [2,4,3], l2 = [5,6,4]
Explanation:
  342 (from l1) + 465 (from l2) = 807
  Output should be [7,0,8]


How to Solve This Problem (Step-by-step Plan)
    Step 1: Initialize variables
            dummy_head – dummy node to start the result list.
            current – pointer to build the result list.
            carry – to hold carryover from addition (initially 0).

    Step 2: Traverse both lists
            Loop while l1, l2, or carry exists.
            Add the values of current nodes and carry.
            Compute the new carry and the digit to store.
            Create a new node with that digit and attach it to the result.

    Step 3: Return result
            After the loop, return dummy_head.next.


Why This Works
This method mimics how we do column addition by hand:

  2 -> 4 -> 3    (342)
+ 5 -> 6 -> 4    (465)
--------------
  7 -> 0 -> 8    (807)
It works for all lengths of input lists and handles carry correctly.

Example Walkthrough: [9,9,9,9,9,9,9] + [9,9,9,9]

Number1: 9999999 -> 9999999
Number2:    9999 ->    9999
Sum:     10009998 -> Output: [8,9,9,9,0,0,0,1]
This shows the carry moving over multiple digits and needing an extra node at the end.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # A dummy node to simplify code
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get current values (or 0 if one list is shorter)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next digit
            current.next = ListNode(total % 10)  # Create a new node with the digit

            # Move pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next
