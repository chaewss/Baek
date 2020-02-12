import java.util.Scanner;

public class $1929 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();

        int[] nums = new int[n+1];
        for (int i = 2; i <= n; i++)
            nums[i] = i;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (nums[i] == 0)
                continue;

            int temp = i;
            for (int j = i+1; j <= n; j++) {
                if (j % temp == 0)
                    nums[j] = 0;
            }
        }

        for (int i = m; i <= n; i++) {
            if (nums[i] != 0)
                System.out.println(nums[i]);
        }
    }
}
