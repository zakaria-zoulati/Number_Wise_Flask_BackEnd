import java.math.BigInteger;

public class Cullen {
    public static boolean isCullenNumber(BigInteger number) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger one = BigInteger.ONE;
        BigInteger n = BigInteger.ZERO;

        while (true) {
            // Generate Cullen number: n * 2^n + 1
            BigInteger powerOfTwo = two.pow(n.intValue());
            BigInteger cullen = n.multiply(powerOfTwo).add(one);

            // If Cullen number equals the input, it's a Cullen number
            if (cullen.equals(number)) {
                return true;
            }

            // If Cullen number exceeds the input, break the loop (no need to continue)
            if (cullen.compareTo(number) > 0) {
                return false;
            }

            // Increment n for the next iteration
            n = n.add(one);
        }
    }

    public static void main(String[] args) {
        BigInteger number = new BigInteger("25"); 

        if (isCullenNumber(number)) {
            System.out.println(number + " is a Cullen number.");
        } else {
            System.out.println(number + " is not a Cullen number.");
        }
    }
}
