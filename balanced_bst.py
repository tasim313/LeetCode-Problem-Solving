# Sorted Linked List to Balanced BST
# Using an Array - O(n) time and O(n) space


class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


class TNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def buildTree(arr, start, end):
    if start > end:
        return None

    mid = (start + end + 1 ) //2
    root = TNode(arr[mid])

    root.left = buildTree(arr, start, mid -1)
    root.right = buildTree(arr, mid + 1, end)

    return root


def sortedListToBST(head):
    arr = []

    while head:
        arr.append(head.data)
        head = head.next
    
    return buildTree(arr, 0, len(arr) - 1)


def printTree(root):
    if not root:
        return
    print(root.data, end=" ")
    printTree(root.left)
    printTree(root.right)


if __name__== "__main__":
    head = LNode(1)
    head.next = LNode(2)
    head.next.next = LNode(3)
    head.next.jnext = LNode(4)
    head.next.next.next = LNode(5)
    head.next.next.next.next = LNode(6)
    head.next.next.next.next.next = LNode(7)

    root = sortedListToBST(head)
    printTree(root)