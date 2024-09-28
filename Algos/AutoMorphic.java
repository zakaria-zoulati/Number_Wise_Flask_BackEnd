public class AutoMorphic {
    public static boolean isAutomorphic(int n){
        int square = n*n ; 
        while( n>0 ){
            if( square % 10 != n % 10 ){
                return false ; 
            }
            square /= 10 ; 
            n /= 10 ; 
        }
        return true ; 
    }
    public static void main( String[] args ){
        int n = 24 ; 
        if( isAutomorphic(n) ){
            System.out.println(n+" Is an automorphic number ") ; 
        }
    }
}