import java.util.Scanner;

public class $8958 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        String[] s = new String[t];
        char[] c = new char[80];
        int cnt = 0; int total = 0;

        for (int i = 0; i < t; i++) {
            s[i] = sc.next();
        }

        for (int i = 0; i < t; i++) {
            total = 0;
            cnt = 0;
            for (int j = 0; j < s[i].length(); j++) {
                c = s[i].toCharArray();
            }
            for (int j = 0; j < s[i].length(); j++) {
                if (c[j] == 'O') {
                    cnt++;
                    total += cnt;
                }
                else if (c[j] == 'X') {
                    cnt = 0;
                }
            }
            System.out.println(total);
        }
    }
}
