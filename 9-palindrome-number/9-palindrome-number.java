class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        else{
            String str = Integer.toString(x);
            String rev = "";
            char ch;
            for (int i=0; i<str.length(); i++)
                {
                    ch= str.charAt(i); 
                    rev= ch+rev;
                }
            if(str.equals(rev)){
                return true;
            }
        }
        return false;
    }
}