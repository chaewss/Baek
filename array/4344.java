import java.util.Scanner;

public class $4344 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        double avg;
        int total, cnt, n;
        int[] scores = new int[1000];

        for (int i = 0; i < c; i++) {
            n = sc.nextInt();
            total = 0; cnt = 0;
            for (int j = 0; j < n; j++) {
                scores[j] = sc.nextInt();
                total += scores[j];
            }
            avg = total / n;
            for (int j = 0; j < n; j++) {
                if (scores[j] > avg)
                    cnt++;
            }
            System.out.printf("%.3f", cnt * 100.0 / n);
            System.out.println("%");
        }
    }
}
