/**
 * Given a string, write a function to determine if it is a permutation of a palindrome
 */

import java.util.*;

public class palindromePermutation
{
    public static void main(String[] args) {
        System.out.println(isPalRetsTrueOdd());
        System.out.println(isPalRetsTrueEven());
        System.out.println(isPalRetsFalseOdd());
        System.out.println(isPalRetsFalseEven());
        System.out.println(preprocessWorks());
    }

    // A permutation of a palindrome would be something where:
    // - If there is an even number of letters, 
    //   each letter should appear an even number of times
    // - If there is an odd number on letters,
    //   each letter *except one* should appear an even amount of times

    public static boolean isPal(String str) {
        char[] proStr = preprocess(str);
        if(proStr.length % 2 == 0) {
            // If even number of characters:
            for(int i = 0; i < proStr.length-1; i+=2) {
                if(proStr[i] != proStr[i+1]) {
                    return false;
                }
            }
            return true;
        } else {
            int unpairedsFound = 0;
            for(int i = 0; i < proStr.length-1; i+=2) {
                if((proStr[i] != proStr[i+1]) && (unpairedsFound > 0)) {
                    return false;
                } else if(proStr[i] != proStr[i+1]) {
                    unpairedsFound++;
                    i--;
                }
            }
            return true;
        }
    }

    public static char[] preprocess(String str) {
        char[] proStr = str.toLowerCase().replaceAll("\\s+","").toCharArray();
        Arrays.sort(proStr);
        return proStr;
    }

    /* TEST METHODS */

    public static int isPalRetsTrueOdd() {
        if(isPal("a cto atc") == true) {
            return 1;
        }
        return 0;
    }

    public static int isPalRetsTrueEven() {
        if(isPal("rat tra") == true) {
            return 1;
        }
        return 0;
    }

    public static int isPalRetsFalseOdd() {
        if(isPal("arbor bear") == false) {
            return 1;
        }
        return 0;
    }

    public static int isPalRetsFalseEven() {
        if(isPal("mean door") == false) {
            return 1;
        }
        return 0;
    }

    public static int preprocessWorks() {
        if(Arrays.equals(preprocess("   a r B  OrB E a r "), "aabbeorrr".toCharArray())) {
            return 1;
        }
        return 0;
    }
}