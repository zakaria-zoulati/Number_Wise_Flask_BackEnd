import java.math.BigInteger;

public class Catalan {

    public static BigInteger catalan(int n) {
        BigInteger numerator = factorial(2 * n);
        BigInteger denominator = factorial(n + 1).multiply(factorial(n));
        return numerator.divide(denominator);
    }

    public static BigInteger factorial(int n) {
        BigInteger fact = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }

    public static boolean isCatalanNumber(BigInteger number) {
        int i = 0;
        while (true) {
            BigInteger catalanNumber = catalan(i);
            if (catalanNumber.equals(number)) {
                return true;
            }
            if (catalanNumber.compareTo(number) > 0) {
                return false;
            }
            i++;
        }
    }

    public static void main(String[] args) {
        BigInteger n = new BigInteger("148800980");
        if (isCatalanNumber(n)) {
            System.out.println(n + " is a Catalan number.");
        } else {
            System.out.println(n + " is not a Catalan number.");
        }
    }
}
