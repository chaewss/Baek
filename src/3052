import java.util.Scanner;

public class $3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num = new int[10];

        for (int i = 0; i < num.length; i++) {
            num[i] = sc.nextInt();
            num[i] %= 42;
        }

        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < i; j++) {
                if (num[i] == num[j]) {
                    num[i] = -1;
                    if (num[i] != num[j])
                        break;
                }
            }
        }
        int cnt = 0;
        for (int i : num) {
            if (i != -1)
                cnt++;
        }
        System.out.println(cnt);
    }
}
