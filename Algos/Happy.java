import java.util.HashSet;
import java.util.Set;

public class Happy {

    public static int pdiFunction(int number, int base) {
        int total = 0;
        while (number > 0) {
            int digit = number % base;
            total += digit * digit; 
            number = number / base;
        }
        return total;
    }

    public static int pdiFunction(int number) {
        return pdiFunction(number, 10); 
    }

    public static boolean isHappy(int number) {
        Set<Integer> seenNumbers = new HashSet<>();
        while (number != 1 && !seenNumbers.contains(number)) {
            seenNumbers.add(number);
            number = pdiFunction(number); 
        }
        return number == 1; 
    }

    public static void main(String[] args) {
        int number = 11 ; 
        if (isHappy(number)) {
            System.out.println(number + " is a happy number.");
        } else {
            System.out.println(number + " is a sad number.");
        }
    }
}
