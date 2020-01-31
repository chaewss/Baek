import java.util.Scanner;

public class $1712 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        long c = sc.nextInt();
        int bp = 0;

        if (c > b) {
            while(c*bp <= a+b*bp) {
                bp++;
                }
            System.out.println(bp);
            }
        else
            System.out.println(-1);
    }
}
