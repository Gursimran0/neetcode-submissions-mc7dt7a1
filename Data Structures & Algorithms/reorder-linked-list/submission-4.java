/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
              ListNode slow = head;
        ListNode fast = head.next;

        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //System.out.println(slow.val);
        ListNode rev = slow.next;
        slow.next = null;
        ListNode prev = null;
        while(rev != null){
            ListNode temp = rev.next;
            rev.next = prev;
            prev = rev;
            rev = temp;
        }
        slow.next = null;
       
        ListNode first = head;
        rev = prev;
        while(rev!=null){
            ListNode temp1 = first.next;
            ListNode temp2 = rev.next;
            first.next = rev;
            rev.next = temp1;
            first = temp1;
            rev = temp2;
            
        }
        
    }
}
