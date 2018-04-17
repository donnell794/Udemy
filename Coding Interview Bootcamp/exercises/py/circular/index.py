# --- Directions
# Given a linked list, return true if the list
# is circular, false if it is not.
# --- Examples
#   const l = new List();
#   const a = new Node('a');
#   const b = new Node('b');
#   const c = new Node('c');
#   l.head = a;
#   a.next = b;
#   b.next = c;
#   c.next = b;
#   circular(l) # true

def circular(li):
    slow = li.head
    fast = li.head
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
