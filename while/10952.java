import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a, b;

        do {
            a = in.nextInt();
            b = in.nextInt();
            if (a == 0 && b == 0)
                break;
            System.out.println(a + b);
        } while (a != 0 && b != 0);
    }
}
