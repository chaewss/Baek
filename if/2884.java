import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int H = in.nextInt();
        int M = in.nextInt();

        M -= 45;
        if (M < 0) {
            if (H != 0) {
                M += 60;
                H -= 1;
            }
            else {
                H = 23;
                M += 60;
            }
        }

        System.out.println(H + " " + M);
    }
}
