/**
 * InnerDoublyLinkedList
 */
// class Node{
//     int head;
//     Node prev;
//     Node next;
    
//     Node (int x){
//     this.head=x;
//     this.next=null;
//     this.prev=null;
//     }
// }
// class Doubly{
//     public static void printl(Node n1) {
//         Node temp = n1;
//         while (temp.next!=null){
//             // System.out.println(temp.prev.head);
//             System.out.println(temp.head);
//             // System.out.println(temp.next.head);
//             temp=temp.next;
//         }
//         System.out.println(temp.head);
//     }

//     Node insertBegin(Node n1,int data){
//         Node x = new Node(data);
//         if(n1 != null){
//           n1.prev=x;
//           x.next=n1;
//           return x;  
//         }
//         else{
//             return x;
//         }
//     }
//     Node insertatEnd(Node n1,int data){
//         Node y = new Node(data);
//         Node temp = n1;
//         while(temp.next!=null){
//             temp=temp.next;
//         }
//         temp.next=y;
//         y.prev=temp;
//         return y;
//     }
//     Node insertatNode(Node n1,Node position,int data){
//         Node y = new Node(data);
//         if(n1==null){
//             return y;
//         }
//         Node temp = n1;
//         while(temp.next!=position){
//             temp=temp.next;
//         }
//         temp.next=y;
//         y.prev=temp;
//         y.next=position;
//         return n1;
//     }
//     Node deleteatBegin(Node n1){
//         if(n1==null){
//             return n1;
//         }
//         Node temp = n1;
//         temp=temp.next;
//         temp.prev=null;
//         return temp;
//     }
//     Node deleteatEnd(Node n1){
//         if(n1==null){
//             return n1;
//         }
//         Node temp = n1;
//         while(temp.next!=null){
//             temp=temp.next; 
//         }
//         temp=temp.prev;
//         temp.next=null;
//         return n1;
//     }
// }


// public class DoublyLinkedList {
//     public static void main(String[] args) {
//         Node n1 = new  Node(10);
//         Node n2 = new  Node(20);
//         Node n3 = new  Node(30);
//         Node n4 = new  Node(40);
//         Node n5 = new  Node(50);
        
//         n1.next=n2;
//         n2.prev=n1;
//         n2.next=n3;
//         n3.prev=n2;
//         n3.next=n4;
//         n4.prev=n3;
//         n4.next=n5;
//         n5.prev=n4;
//         // System.out.println(n1.head);
//         // // System.out.println((n1.next));
        

//         Doubly d = new Doubly();
//         Node p = d.insertBegin(n1, 30);
//         Node q = d.insertatEnd(n1, 100);
//         Node r = d.insertatNode(n1, n3, 69);
//         // Node s = d.deleteatBegin(n1);
//         Node t = d.deleteatEnd(n1);
//         Doubly.printl(n1);
//     }
// }
