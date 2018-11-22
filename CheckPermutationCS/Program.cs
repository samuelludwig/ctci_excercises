using System;

namespace CheckPermutationCS
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(isCheckPermReturningTrueWhenStringsArePermutations());
            Console.WriteLine(isCheckPermReturningFalseWhenStringsAreNotPermutations());
        }

        static bool checkPermutation(String str1, String str2) {
        if (str1.Length != str2.Length) {
            return false;
        }

        char[] firstStr = str1.ToCharArray();
        char[] secondStr = str2.ToCharArray();

        Array.Sort(firstStr);
        Array.Sort(secondStr);

        for (int i = 0; i < str1.Length; i++) {
            if (firstStr[i] != secondStr[i]) {
                return false;
            }
        }
        
        return true;
    }

    
    /* --- --- TESTS --- --- */

    static bool isCheckPermReturningTrueWhenStringsArePermutations() {
        if(checkPermutation("barrel", "rerlab") == true) {
            return true;
        }
        
        return false;
    }

    static bool isCheckPermReturningFalseWhenStringsAreNotPermutations() {
        if(checkPermutation("racecar", "orange") == false) {
            return true;
        }
        
        return false;
    }
    }
}
