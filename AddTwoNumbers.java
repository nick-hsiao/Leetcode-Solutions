/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    //init variables and set nodes m1,m2 to head of list
    int carry = 0; 
		int m1val, m2val, sum;
		ListNode m1 = l1;
		ListNode m2 = l2;
		ListNode result = new ListNode(0);
		ListNode r = result;
		boolean done = false;
    
		while(!done) {
			m1val = (m1 != null) ? m1.val : 0; //get vals from node if the exist, 0 otherwise 
			m2val = (m2 != null) ? m2.val : 0;
			sum = (m1val+m2val+carry)%10; //add vals
			carry = (m1val+m2val+carry)/10; //check for carry
			r.val = sum;
			if (m1.next == null && m2.next == null && carry == 0) // end of both lists and no carry
			{
				done = true;
				break;
			} 
			m1 = (m1.next != null) ? m1.next : new ListNode(0); //if m1 or m2 does not exist, replace with new node value 0
			m2 = (m2.next != null) ? m2.next : new ListNode(0);
			r.next = new ListNode(0);
			r = r.next; //iterate to next node in the list
			
		}
		return result;    
}
}
