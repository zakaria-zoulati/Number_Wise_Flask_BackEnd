public class Triangular {
    public static boolean isTriangular(int n) {
        int discriminant = 1 + 8 * n;
        int sqrtDiscriminant = (int) Math.sqrt(discriminant);
        return (sqrtDiscriminant * sqrtDiscriminant == discriminant) && ((-1 + sqrtDiscriminant) % 2 == 0);
    }
    public static void main(String[] args) {
        int number = 10; // Example number to check
        if (isTriangular(number)) {
            System.out.println(number + " is a triangular number.");
        } else {
            System.out.println(number + " is not a triangular number.");
        }
    }
}