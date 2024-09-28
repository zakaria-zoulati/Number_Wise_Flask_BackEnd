import java.math.BigInteger;

public class Palindromic {

    public static boolean isPalindrome(BigInteger number) {
        String original = number.toString();
        String reversed = new StringBuilder(original).reverse().toString();
        return original.equals(reversed);
    }

    public static void main(String[] args) {
        BigInteger n = new BigInteger("12321"); 
        if (isPalindrome(n)) {
            System.out.println(n + " is a palindromic number.");
        } else {
            System.out.println(n + " is not a palindromic number.");
        }
    }
}
