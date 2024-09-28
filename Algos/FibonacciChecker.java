public class FibonacciChecker {

    public static boolean isPerfectSquare(int x) {
        int s = (int) Math.sqrt(x);
        return (s * s == x);
    }
    public static boolean isFibonacci(int n) {
        return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);
    }

    public static void main(String[] args) {
        int number = 21; 
        if (isFibonacci(number)) {
            System.out.println(number + " is a Fibonacci number.");
        } else {
            System.out.println(number + " is not a Fibonacci number.");
        }
    }
}
