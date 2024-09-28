public class Pentagonal {
    public static boolean isPentagonal(int number) {
        double n = (1 + Math.sqrt(1 + 24 * number)) / 6;
        return n == Math.floor(n) && n > 0;
    }

    public static void main(String[] args) {
        int n = 12; 
        if (isPentagonal(n)) {
            System.out.println(n + " is a pentagonal number.");
        } else {
            System.out.println(n + " is not a pentagonal number.");
        }
    }
}
