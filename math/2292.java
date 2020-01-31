import java.util.Scanner;

public class $2292 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        int move = 1;
        int add = 6;
        int finroom = 1;

        while(true) {
            if (num <= finroom)
                break;

            finroom += add;
            add += 6;
            move++;
        }
        System.out.println(move);
    }
}
