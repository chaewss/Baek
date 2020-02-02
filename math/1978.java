import java.util.Scanner;

public class $1978 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sosuCnt = 0, cnt = 0;

        for (int i = 1; i <= n; i++) {
            int num = sc.nextInt();
            sosuCnt = 0;

            for (int j = 1; j <= num; j++) {
                if (num % j == 0)
                    sosuCnt++;
            }

            if (sosuCnt == 2)
                cnt++;
        }
        System.out.print(cnt);
    }
}
