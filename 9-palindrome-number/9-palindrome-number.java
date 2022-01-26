class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        else{
            String str = Integer.toString(x);
            for(int i=0;i<str.length()/2;i++){
                if(str.charAt(i)!=str.charAt(str.length()-i-1)){
                    return false;
                }
            }
            return true;
        }
    }
}