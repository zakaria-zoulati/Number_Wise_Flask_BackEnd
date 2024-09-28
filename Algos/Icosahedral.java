public class Icosahedral{

    public static boolean isIcosahedral(int number) {
        if (number < 0) {
            return false;
        }
        for (int n = 0; ; n++) {
            int first = (5 * n * n * n - 5 * n * n + 2 * n) ; 
            if( first % 2 == 1 ) continue ; 
            int icosahedral = first / 2;
            if (icosahedral == number) {
                return true; 
            }
            if (icosahedral > number) {
                break; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        int n = 48 ; 

        if (isIcosahedral(n)) {
            System.out.println(n + " is an icosahedral number.");
        } else {
            System.out.println(n + " is not an icosahedral number.");
        }
    }
}
