import java.util.Scanner;

public class $3009 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] array = new int[6];
        int fx = 0;  int fy = 0;
        int x = 0;  int y = 0;
        for (int i = 0; i < 6; i++) {
            array[i] = in.nextInt();
        }

        for (int i = 0; i < 4; i+=2) {
            for (int j = i+2; j < 6; j+=2) {
                if (array[i] == array[j])
                    fx = array[i];
            }
        }
        for (int i = 0; i < 6; i+=2) {
                if (array[i] != fx)
                    x = array[i];
        }

        for (int i = 1; i < 5; i+=2) {
            for (int j = i+2; j <= 6; j+=2) {
                if (array[i] == array[j]){
                    fy = array[i];
                }
            }
        }
        for (int i = 1; i <= 6; i+=2) {
            if (array[i] != fy) {
                y = array[i];
            }
        }
        System.out.printf("%d %d", x, y);

    }
}
