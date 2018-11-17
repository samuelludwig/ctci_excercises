/**
 * Implement an algorithm to determine if a string has all unique characters.
 */
import java.util.*;
import java.lang.*;

public class isUnique {

    public static void main(String[] args) {
        System.out.println(isErrorGivenWithNoString());
        System.out.println(isStringProcessedCorrectly());
        System.out.println(isStringIsUniqueReturningFalseOnNonUniqueLetter());
        System.out.println(isStringIsUniqueReturningTrueWithAllUniqueLetters());
    }

    static String processInput(String s) {
        if (s.equals("")) {
            return "Error, invalid string!";
        }

        return s.toLowerCase();
    }

    static boolean stringIsUnique(String s) {
        processInput(s);
        char[] carr = s.toCharArray();

        Arrays.sort(carr);

        for (int i = 0; i < (s.length() - 1); i++) {
            if (carr[i] == carr[i+1]) {
                return false;
            }
        }
        
        return true;
    }

    
    /* --- TESTS --- */

    // Test that an error message is given if no String is supplied
    static boolean isErrorGivenWithNoString() {
        if (processInput("").equals("Error, invalid string!")) {
            return true;
        }
        return false;
    }

    // Test that the provided String is converted correctly into lowercase
    static boolean isStringProcessedCorrectly() {
        if (processInput("HEllO").equals("hello")) {
            return true;
        }
        return false;
    }


    // Test that stringIsUnique() returns false when a non-unique letter is encountered
    static boolean isStringIsUniqueReturningFalseOnNonUniqueLetter() {
        if (stringIsUnique("Hello") == false) {
            return true;
        }

        return false;
    }
    
    // Test that stringIsUnique() returns true when a unique string is passed through
    static boolean isStringIsUniqueReturningTrueWithAllUniqueLetters() {
        if (stringIsUnique("mango") == true) {
            return true;
        }

        return false;
    }

}