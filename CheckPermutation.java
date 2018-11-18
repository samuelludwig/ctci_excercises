/**
 * Check if two strings are permutations of one another
 */

import java.util.*;
import java.lang.*;

public class CheckPermutation {

    public static void main(String[] args) {
        System.out.println(isCheckPermReturningTrueWhenStringsArePermutations());
        System.out.println(isCheckPermReturningFalseWhenStringsArePermutations());
    }

    static boolean checkPermutation(String str1, String str2) {
        return true;
    }

    
    /* --- --- TESTS --- --- */

    static boolean isCheckPermReturningTrueWhenStringsArePermutations() {
        if(checkPermutation("barrel", "rerlab") == true) {
            return true;
        }
        
        return false;
    }

    static boolean isCheckPermReturningFalseWhenStringsArePermutations() {
        if(checkPermutation("racecar", "orange") == false) {
            return true;
        }
        
        return false;
    }
}