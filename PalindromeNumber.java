//Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || x % 10 == 0 && x!=0){
            return false;
        }
        int ans = 0;
        while (x > ans){
            ans = ans * 10 + x % 10;
            x /= 10;
        }
        
        return x == ans || x == ans/10;
        
    }
}