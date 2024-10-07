public class Pronic {

    public static boolean isPronic(int number) {
        if (number < 0) {
            return false;
        }
        for (int n = 0; n * (n + 1) <= number; n++) {
            if (n * (n + 1) == number) {
                return true; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int n = 20; 

        if (isPronic(n)) {
            System.out.println(n + " is a pronic number.");
        } else {
            System.out.println(n + " is not a pronic number.");
        }
    }
}
