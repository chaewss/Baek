import java.util.Scanner;

public class $2839 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = n/5;

        for (int i = a; i >= 0; i--) {
            if (5 * i == n) {
                System.out.println(i);
                return;
            }
            else {
                for (int j = 0; j <= (n-5*i)/3; j++) {
                    if (3*j == (n-5*i)) {
                        System.out.println(i + j);
                        return;
                    }
                    else {
                        if (i == 0 && j == (n - 5 * i) / 3 && 5 * i + 3 * j != n) {
                            System.out.println(-1);
                        }
                        continue;
                    }
                }
            }
        }
    }
}
