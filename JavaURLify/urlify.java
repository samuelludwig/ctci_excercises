/**
 *  Write a method to replace all spaces in a string with '%20'. 
 *  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given
 *  the true length of the string.
 */

import java.util.Arrays;
public class urlify {

    public static void main(String[] args) {
        System.out.println(urlifyReturnsUrlifiedStringWhenSpacesPresent());
        System.out.println(urlifyReturnsEmptyStringIfEmptyStringIsProvided());
        System.out.println(urlifyReturnsUnalteredStringIfNoSpaces());
    }

    public static char[] urlifyString(String url, int tLength) {
        char[] urlArr = url.toCharArray();
        for (int i = 0; i < tLength; i++) {
            if (urlArr[i] == ' ') {
                for (int j = (urlArr.length - 1); j > i; j--) {
                    urlArr[j] = urlArr[j-2];
                }
                urlArr[i] = '%';
                urlArr[i+1] = '2';
                urlArr[i+2] = '0';
                tLength = tLength+2;
            }
        }
<<<<<<< HEAD
        
=======
>>>>>>> c813f9ad54528a04ab884d087c5e4cff8a253456
        return urlArr;
    }

    // TESTS //
    static boolean urlifyReturnsUrlifiedStringWhenSpacesPresent() {
        if (Arrays.equals(urlifyString("c a t    ", 5), ("c%20a%20t".toCharArray()))) {
            return true;
        } else {
            return false;
        }
    }

    static boolean urlifyReturnsEmptyStringIfEmptyStringIsProvided() {
        if (Arrays.equals(urlifyString("", 0), ("".toCharArray()))) {
            return true;
        } else {
            return false;
        }
    }
    
    static boolean urlifyReturnsUnalteredStringIfNoSpaces() {
        if (Arrays.equals(urlifyString("cat", 3), ("cat".toCharArray()))) {
            return true;
        } else {
            return false;
        }
    }
}