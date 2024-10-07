public class Pentatope {
    public static boolean isPentatope(int number) {
        if (number < 0) {
            return false; 
        }
        for (int n = 0; ; n++) {
            int pentatope = (n * (n + 1) * (n + 2) * (n + 3)) / 24;
            if (pentatope == number) {
                return true; 
            }
            if (pentatope > number) {
                break; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int n = 35; 
        if (isPentatope(n)) {
            System.out.println(n + " is a pentatope number.");
        } else {
            System.out.println(n + " is not a pentatope number.");
        }
    }
}
