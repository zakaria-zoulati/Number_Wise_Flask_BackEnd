public class Octagonal {

    public static boolean isOctagonal(int number) {
        if (number < 0) {
            return false;
        }
        for (int n = 0; ; n++) {
            int octagonal = n * (3 * n - 2);
            if (octagonal == number) {
                return true; 
            }
            if (octagonal > number) {
                break; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int n = 21; 
        if (isOctagonal(n)) {
            System.out.println(n + " is an octagonal number.");
        } else {
            System.out.println(n + " is not an octagonal number.");
        }
    }
}
