import java.util.Scanner;

public class $4948 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true) {
            int n = sc.nextInt();
            int m = n * 2;
            int cnt = 0;

            if (n == 0)
                break;

            int[] nums = new int[m+1];
            for (int i = 2; i <= m; i++)
                nums[i] = i;

            for (int i = 2; i <= Math.sqrt(m); i++) {
                if (nums[i] == 0)
                    continue;

                int temp = i;
                for (int j = i+1; j <= m; j++) {
                    if (j % temp == 0)
                        nums[j] = 0;
                }
            }

            for (int i = n+1; i < nums.length; i++) {
                if (nums[i] != 0)
                    cnt++;
            }
            System.out.println(cnt);
        }
    }
}
