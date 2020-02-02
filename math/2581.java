import java.util.Scanner;

public class $2581 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int sosuCnt = 0;    int cnt = 0;
        int min = 10000;    int sum = 0;

        for(int i = m; i <= n; i++) {
            sosuCnt = 0;

            for (int j = 1; j <= i; j++) {
                if (i % j == 0)
                    sosuCnt++;
            }

            if (sosuCnt == 2) {
                if (i < min)
                    min = i;

                sum += i;
                cnt++;
            }
        }
        if (cnt == 0)
            System.out.println(-1);
        else {
            System.out.println(sum);
            System.out.println(min);
        }

    }
}
