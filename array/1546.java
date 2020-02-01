import java.util.Scanner;

public class $1546 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        double[] score = new double[num];
        double m = 0, sum = 0, average = 0;

        for (int i = 0; i < num; i++) {
            score[i] = in.nextInt();
            if (m < score[i])
                m = score[i];
        }

        for (int i = 0; i < num; i++) {
            score[i] = score[i] / m * 100;
            sum += score[i];
        }

        average = sum / num;
        System.out.printf("%.2f", average);
    }
}
