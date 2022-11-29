def isPalindrome(self, head):
    """pal=[]
        while head:
            pal.append(head.val)
            head = head.next

        l,r = 0, len(pal) -1

        while l <= r:
            if pal[l] != pal[r]:
                return False
            l+=1
            r-=1
        return True"""
    fast = head
    slow = head
    # finding middle (slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reversing linked list
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    l, r = head, prev

    while r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True
