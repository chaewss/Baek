import java.util.Scanner;

public class $2869 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); // 낮에 올라간 길이
        int b = sc.nextInt(); // 밤에 미끄러진 길이
        int v = sc.nextInt(); // 올라가야 하는 총길이
        int current = 0;    int day = 0;

        if ((v-a) % (a-b) == 0) {
            day = (v-a) / (a-b);
        }
        else {
            day = (v-a) / (a-b) + 1;
        }
        day++;
        System.out.println(day);
    }
}
