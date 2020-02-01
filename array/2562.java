import java.util.Scanner;

public class $2562 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] array = new int[10];
        int max = array[0], mi = 0;
        for (int i = 1; i < 10; i++)
            array[i] = in.nextInt();

        for (int i = 1; i < 10; i++) {
            if (max < array[i]) {
                max = array[i];
                mi = i;
            }
        }
        System.out.println(max);
        System.out.println(mi);
    }
}
