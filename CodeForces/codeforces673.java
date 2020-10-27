// package CodeForces;

// import java.util.Scanner;
// import java.lang.Math;

// public class codeforces673 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int t = sc.nextInt();
//         for (int jk = 0; jk < t; jk++) {
//             int n = sc.nextInt();
//             int k = sc.nextInt();
//             int[] arr = new int[n];
//             int maxx = 100000;
//             for (int j = 0; j < n; j++) {
//                 int km = sc.nextInt();
//                 arr[j] = k - km;
//                 maxx = Math.min(maxx, km);
//             }
//             int mic = 0;
//             int op = 0;
//             for (int i = 0; i < n; i++) {
//                 if (arr[i] == (k - maxx) && mic == 0)
//                     mic++;
//                 else
//                     op += (int) arr[i] / maxx;
//             }
//             System.out.println(op);
//         }
//         sc.close();
//     }
// }