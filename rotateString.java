//We are given two strings, A and B.

//A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

class Solution {
    public boolean rotateString(String A, String B) {
        if (A.equals(B)){
            return true;
        }
        int length = A.length();
        for (int i = 0; i < length; i++){
            A = A.substring(1,length) + A.substring(0,1);
            if (A.equals(B)){
                return true;
            }
        }
        return false;
    }
}