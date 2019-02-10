/**
 *  Write a method to replace all spaces in a string with '%20'. 
 *  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given
 *  the true length of the string.
 */
public class urlify {

    public static void main(String[] args) {
        System.out.println(urlifyReturnsUrlifiedStringWhenSpacesPresent());
        System.out.println(urlifyReturnsEmptyStringIfEmptyStringIsProvided());
        System.out.println(urlifyReturnsUnalteredStringIfNoSpaces());
    }

    public static String urlifyString(String url, int tLength) {
        char[] urlArr = url.toCharArray();
        for (int i = 0; i < tLength; i++) {
            if (urlArr[i] == ' ') {
                for (int j = (urlArr.length - 1); j > i; j--) {
                    urlArr[j] = urlArr[j-2];
                }
                urlArr[i] = '%';
                urlArr[i+1] = '2';
                urlArr[i+2] = '0';
            }
        }
        
        return urlArr;
    }

    // TESTS //
    static boolean urlifyReturnsUrlifiedStringWhenSpacesPresent() {
        if (urlifyString("c a t    ", 5).equals("c%20a%20t")) {
            return true;
        } else {
            return false;
        }
    }

    static boolean urlifyReturnsEmptyStringIfEmptyStringIsProvided() {
        if (urlifyString("", 0).equals("")) {
            return true;
        } else {
            return false;
        }
    }
    
    static boolean urlifyReturnsUnalteredStringIfNoSpaces() {
        if (urlifyString("cat", 3).equals("cat")) {
            return true;
        } else {
            return false;
        }
    }
}