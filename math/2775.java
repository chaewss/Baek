import java.util.Scanner;

public class $2775 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int tc = in.nextInt();

        int sum = 0;

        for (int i = 0; i < tc; i++) {
            int k = in.nextInt();
            int n = in.nextInt();
            int[][] apart = new int[16][16];

            for (int o = 1; o <= n; o++) // 0층 인원수 저장
                apart[0][o] = o;

            for (int j = 1; j <= k; j++) {
                for (int o = 1; o <= n; o++) {
                    sum = 0;
                    for (int p = 1; p <= o; p++) {
                        sum += apart[j-1][p];
                        apart[j][o] = sum;
                    }
                }
            }

            System.out.println(apart[k][n]);
        }
    }
}
