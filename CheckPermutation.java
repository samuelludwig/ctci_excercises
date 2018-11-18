/**
 * Check if two strings are permutations of one another
 */

import java.util.*;
import java.lang.*;

public class CheckPermutation {

    public static void main(String[] args) {
        System.out.println(isCheckPermReturningTrueWhenStringsArePermutations());
        System.out.println(isCheckPermReturningFalseWhenStringsAreNotPermutations());
    }

    static boolean checkPermutation(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }

        char[] firstStr = str1.toCharArray();
        char[] secondStr = str2.toCharArray();

        Arrays.sort(firstStr);
        Arrays.sort(secondStr);

        for (int i = 0; i < str1.length(); i++) {
            if (firstStr[i] != secondStr[i]) {
                return false;
            }
        }
        
        return true;
    }

    
    /* --- --- TESTS --- --- */

    static boolean isCheckPermReturningTrueWhenStringsArePermutations() {
        if(checkPermutation("barrel", "rerlab") == true) {
            return true;
        }
        
        return false;
    }

    static boolean isCheckPermReturningFalseWhenStringsAreNotPermutations() {
        if(checkPermutation("racecar", "orange") == false) {
            return true;
        }
        
        return false;
    }
}
