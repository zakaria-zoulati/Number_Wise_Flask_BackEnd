public class Harshad {

    public static int sumOfDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10; 
            number = number / 10; 
        }
        return sum;
    }

    public static boolean isHarshad(int number) {
        int sum = sumOfDigits(number);
        return (number % sum == 0);  
    }

    public static void main(String[] args) {
        int number = 18; 
        if (isHarshad(number)) {
            System.out.println(number + " is a Harshad number.");
        } else {
            System.out.println(number + " is not a Harshad number.");
        }
    }
}
