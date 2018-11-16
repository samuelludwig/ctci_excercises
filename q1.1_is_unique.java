/**
 * Implement an algorithm to determine if a string has all unique characters.
 */
public class IsUnique {

    public static void main(String[] args) {
        
    }

    boolean stringIsUnique(String s) {
        
        return true;
    }

    
    /* --- TESTS --- */

    // Test that an error message is given if no String is supplied
    boolean isErrorGivenWithNoString() {
        return false;
    }

    // Test that stringIsUnique() returns false when a non-unique letter is encountered
    boolean isStringIsUniqueReturningFalseOnNonUniqueLetter() {
        if (stringIsUnique("Hello") == false) {
            return true;
        }

        return false;
    }
    
    boolean isStringIsUniqueReturningTrueWithAllUniqueLetters() {
        if (stringIsUnique("mango") == true) {
            return true;
        }

        return false;
    }

}
