import java.math.BigInteger;

public class Fermat{
    public static boolean isFermatNumber(BigInteger number) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger one = BigInteger.ONE;
        int n = 0;
        while (true) {
            BigInteger exponent = two.pow(two.pow(n).intValue()); // 2^(2^n)
            BigInteger fermat = exponent.add(one); // 2^(2^n) + 1
            if (fermat.equals(number)) {
                return true;
            } else if (fermat.compareTo(number) > 0) {
                return false;
            }
            n++;
        }
    }
    public static void main(String[] args) {
        BigInteger number = new BigInteger("18446744073709551617");
        if (isFermatNumber(number)) {
            System.out.println(number + " is a Fermat number.");
        } else {
            System.out.println(number + " is not a Fermat number.");
        }
    }
}
