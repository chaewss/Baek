import java.util.Scanner;

public class $2577 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int result = a * b * c;
        int[] cntarr = new int[10];

        while (result > 0) {
            cntarr[result % 10]++;
            result/= 10;
        }

        for (int i : cntarr)
            System.out.println(i);

    }
}
