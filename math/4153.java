import java.util.Arrays;
import java.util.Scanner;

public class $4153 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        while (true) {
            int[] num = new int[3];
            for (int i = 0; i < 3; i++)
                num[i] = in.nextInt();

            if (num[0] == 0 && num[1] == 0 && num[2] == 0)
                break;
            else {
                Arrays.sort(num);
                if (Math.pow(num[0], 2) + Math.pow(num[1], 2) == Math.pow(num[2], 2))
                    System.out.println("right");
                else
                    System.out.println("wrong");
            }
        }
    }
}
