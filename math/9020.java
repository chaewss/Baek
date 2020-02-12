import java.util.ArrayList;
import java.util.Scanner;

public class $9020 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        for (int i = 0; i < t; i++) {
            int n = in.nextInt();

            if (n%2 != 0 || n < 4 || n > 10000)
                break;
            else {
                int[] nums = new int[n + 1];

                for (int j = 2; j <= n; j++)
                    nums[j] = j;

                for (int j = 2; j <= Math.sqrt(n); j++) {
                    if (nums[j] == 0)
                        continue;

                    int temp = j;
                    for (int k = j + 1; k <= n; k++) {
                        if (k % temp == 0)
                            nums[k] = 0;
                    }
                }

                ArrayList<Integer> list = new ArrayList<>();
                for (int j = 2; j <= n; j++) {
                    if (nums[j] != 0)
                        list.add(nums[j]);
                }

                int a = 0;  int b = 0;
                int min = 10000;
                loop:
                for (int j = list.size()-1; j >= 0; j--) {
                    for (int k = j; k < list.size(); k++) {
                        if (list.get(j)+list.get(k) == n) {
                            if (list.get(k)-list.get(j) > min)
                                break loop;

                            if (list.get(k)-list.get(j) <= min) {
                                a = list.get(j);
                                b = list.get(k);
                                min = list.get(k)-list.get(j);
                            }
                        }
                    }
                }
                System.out.printf("%d %d\n", a, b);
            }
        }
    }
}
