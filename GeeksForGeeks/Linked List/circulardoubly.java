// class Node{
//     int head;
//     Node next;
//     Node prev;

//     Node(int data){
//         this.head=data;
//         this.next=null;
//         this.prev=null;
//     }
// }

// class CircularDoub{
//     public static void printL(Node n1) {
//         Node temp = n1;
//         while(temp.next != n1){
//             System.out.print(temp.head + "|*|");
//             temp=temp.next;
//         }
//         System.out.print(temp.head+ "|*|");
//         System.out.println(temp.next.head);
//     }
//     Node Insertatany(Node position,int x){
//         Node temp = new Node(x);
//         Node y = position.prev;
//         y.next=temp;
//         temp.next=position;
//         position.prev=temp;
//         return position;
//     }
// }


// /**
//  * circulardoubly
//  */
// public class circulardoubly {

//     public static void main(String[] args) {
//         Node n1 = new Node(10);
//         Node n2 = new Node(20);
//         Node n3 = new Node(30);
//         Node n4 = new Node(40);

//         n1.next=n2;
//         n2.next=n3;
//         n3.next=n4;
//         n4.next=n1;
//         n1.prev=n4;
//         n2.prev=n1;
//         n3.prev=n2;
//         n4.prev=n3;

//         CircularDoub cd = new CircularDoub();
//         Node z = cd.Insertatany(n2, 69);
//         cd.printL(z);
//     }
// }