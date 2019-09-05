//Given a linked list, remove the n-th node from the end of list and return its head.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null){
            return null;
        }
        HashMap<Integer,ListNode> map = new HashMap<Integer,ListNode>();
        int i = 0;
        ListNode curr = head;
        while (curr != null){
            i++;
            map.put(i,curr);
            curr = curr.next;
        
        }
        if (i-n == 0){
            return head.next;
        }
        ListNode prev = map.get(i-n);
        ListNode next = null;
        if (prev.next != null){
            next = prev.next.next;
        }
        
        
        prev.next = next;
        return head;
    }
}