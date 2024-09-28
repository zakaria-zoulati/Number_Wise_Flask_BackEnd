public class Prime {
    public boolean isPrime(int n) {
        if (n < 2) {
            return false; 
        }
        if (n == 2 || n == 3) {
            return true; 
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false; 
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int n = 113;
        Prime p = new Prime();
        if (p.isPrim(n)) {
            System.err.println("Yes, the number " + n + " is prime");
        } else {
            System.err.println("The number " + n + " is not prime");
        }
    }
}
