public class Lucas {
    public static boolean isLucas(int number) {
        if (number < 0) {
            return false; 
        }

        int a = 2; 
        int b = 1; 

        if (number == a || number == b) {
            return true; 
        }
        int lucasNumber = 0;
        while (lucasNumber < number) {
            lucasNumber = a + b; 
            a = b; 
            b = lucasNumber;

            if (lucasNumber == number) {
                return true; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int n = 11; 
        if (isLucas(n)) {
            System.out.println(n + " is a Lucas number.");
        } else {
            System.out.println(n + " is not a Lucas number.");
        }
    }
}
