import java.util.Scanner;

public class $10250 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); //테스트 데이터 개수
        String answer = "";  int cnt = 0;

        for (int k = 0; k < t; k++) {
            cnt = 0;
            int h = sc.nextInt(); //호텔 층 수
            int w = sc.nextInt(); //각 층의 방 수
            int n = sc.nextInt(); //몇 번째 손님
            loop:
            for (int i = 1; i <= w; i++) {
                for (int j = 1; j <= h; j++) {
                    cnt++;
                    if (cnt == n) {
                        if (i / 10 == 0)
                            answer = Integer.toString(j) + "0" + Integer.toString(i);
                        else
                            answer = Integer.toString(j) + Integer.toString(i);
                        break loop;
                    }
                }
            }
            System.out.println(answer);
        }

    }
}
