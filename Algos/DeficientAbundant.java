public class DeficientAbundant {
    public static void main( String[] args ){
        // int n = 47 ; 
        int n = 48 ; 
        int sum = 0 ; 
        for(int i=1 ; i<=n/2 ; ++i){
            if( n % i == 0 ){
                sum += i ;
            }
        }
        if( sum <= n ){
            System.out.println("The number "+n+" Is deficient");
        }else{
            System.out.println("The number "+n+" is Abundant" ) ; 
        }
    }
}