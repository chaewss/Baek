import java.util.Scanner;

public class $10818 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int max = -1000000;
        int min = 100000;

        if (n >= 1 && n <= 1000000) {
            int[] a = new int[n];
            for(int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            for (int j : a) {
                if (j > max)
                    max = j;
                if (j < min)
                    min = j;
            }
        }
        System.out.println(min + " " + max);
    }
}
