public class Polite {
    public static boolean isPolite( int n  ){
        if( ( n & ( n-1 ) ) == 0  ){
            return false ;
        }  
        return true ; 
    }
    public static void main(String[] args){
        int n = 4 ; 
        if( isPolite(n) ){
            System.out.println(n+" Is a Polite number") ; 
        }
    }
}