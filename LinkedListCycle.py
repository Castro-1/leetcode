def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow, fast = head
    while fast and fast.next != None:
        slow.next
        fast.next.next
        if slow == fast:
            return True
    return False
