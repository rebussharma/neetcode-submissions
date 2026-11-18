class Solution {
    public boolean isAlnum(char t){
        int asc = (int) t;
        if (65 <= asc && asc <= 90){
            return true;
        }
        else if(97 <= asc && asc <= 122){
            return true;
        }
        else if(asc >= 48 && asc <= 57){
            return true;
        }
        return false;
    }

    public boolean isPalindrome(String s) {
        /*
            1: ignore non alnum => isAlNum()?
            2: ignore case => toLower()

            // madam
            1. reverse the string
            2. check if each element is same

            // abba

            1. loop from start of the array
            2. loop from end of the array
            3. loop until we reach the middle ground or items arent same
            4. return true at the end

            #b*
            l = 0
            r = 2

            l = 1
            r = 1
        */

        int l = 0;
        int r = s.length() - 1;

        while(l < r){
            if(!isAlnum(s.charAt(l))){
                l += 1; //a
            }
            else if(!isAlnum(s.charAt(r))){
                r -= 1;
            }
            else if (Character.toLowerCase(s.charAt(l)) == Character.toLowerCase(s.charAt(r))) {
                l += 1;
                r -= 1;
            }
            else{
                return false;
            }

        }
        return true;
    }

}
