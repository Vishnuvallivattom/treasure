class Solution(object):
    def hasCycle(self, head):
        f = head         # 'f' is the fast pointer
        s = head         # 's' is the slow pointer

        while(f != None and f.next != None):
            s = s.next           # slow pointer moves by 1 step
            f = f.next.next      # fast pointer moves by 2 steps

            if s == f:
                return True      # cycle detected

        # if we exit the loop, no cycle is present
