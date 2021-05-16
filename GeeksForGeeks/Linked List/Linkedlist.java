class Node{
    int head;
    Node next;
    Node (int x){
        this.head=x;
        this.next=null;
    }
}

class LinkedListOperation{
    public void ntheNode(Node n1, int x) {
        Node temp = n1;
        int count = 1;
        while (temp.next != null) {
            count++;
            temp = temp.next;
        }
        Node ttemp=n1;
        int l = 0;
        while (l < count - x ) {
            ttemp = ttemp.next;
            l++;
        }
        System.out.println(ttemp.head);
    }

    void printl(Node n1) {
        Node temp = n1;
        while (temp.next != null) {
            System.out.print(temp.head + "||");
            temp = temp.next;
        }
        System.out.println(temp.head);
    }
    Node reverse(Node n1){
        Node temp = n1;
        Node x = null;
        while(temp!=null){
            Node next=temp.next;
            temp.next=x;
            x=temp;
            temp=next;
        }
        return x;    
    }
}

/**
 * Linkedlist
 */
public class Linkedlist {
    public static void main(String[] args) {
        Node n1 = new Node(10);
        Node n2 = new Node(20);
        Node n3 = new Node(30);
        n1.next = n2;
        n2.next = n3;

        LinkedListOperation ll = new LinkedListOperation();
        ll.printl(n1);
        ll.ntheNode(n1, 2);
        Node z = ll.reverse(n1);
        ll.printl(z);
    
    }
    
}
