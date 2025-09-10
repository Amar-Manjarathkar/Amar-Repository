/*
class Node {
    int data;
    Node next;
    Node(int x) {
        data = x;
        next = null;
    }
}*/

class Solution {
    public ArrayList<Integer> printList(Node head) {
        // code 
        ArrayList<Integer> result = new ArrayList<>();
        Node current = head;
        
        while(current!=null){
            result.add(current.data);
            current=current.next;
        }
        return result;
        
    }
}
