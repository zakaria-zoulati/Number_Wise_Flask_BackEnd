public class Prime {

    public static int sumOfDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    public static boolean isSmithNumber(int number) {
        int digitSum = sumOfDigits(number);
        int p  = primeFactorSum(number);
        return digitSum == p;
    }

    static int primeFactorSum(int n) {
        int sum = 0;
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                sum += sumOfDigits(i);
                n /= i;
            }
        }
        return sum;
    }

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

    public static boolean isMersennePrine( int n  ){
        int power = 0;
        int num = n + 1;  
        while (num % 2 == 0) {
            num /= 2;
            power++;
        }
        return num == 1 && power > 0;
    }
    public static void main(String[] args) {
        int n = 4937775 ;
        Prime p = new Prime();
        if (p.isPrime(n)) {
            System.out.println("The number " + n + " is prime");
            if( isMersennePrine(n) ){
                System.out.println("The number "+n+" Is a Mersenne Prime") ; 
            }
            if( p.isPrime( 2 * n + 1 ) ){
                System.out.println( n + " Is a Sophie Germain prime" ) ; 
            }
        } else {
            System.out.println("The number " + n + " is a composite number");
            if( isSmithNumber(n) ){
                System.out.println("The number "+n+" is a Smith number");
            }
        }
    }
}
