import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class $1085 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        int x = in.nextInt();
        int y = in.nextInt();
        int w = in.nextInt();
        int h = in.nextInt();

        list.add(x);
        list.add(y);
        list.add(w-x);
        list.add(h-y);
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}
