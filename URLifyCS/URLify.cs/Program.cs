using System;

namespace URLify.cs
{
    class Program   
    /*  
        Write a method to replace all spaces in a string with '%20'. 
        You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given
        the true length of the string.
    */ 
    {
        static void Main(string[] args)
        {
            Console.WriteLine(isReturningURLifiedString());
            Console.WriteLine(isReturningUnchangedStringIfNoSpaces());
        }

        static string urlify(int length, string str) 
        {
            char[] myStr = str.ToCharArray();
            for (int i = 0; i < length; i++) {
                // check if I'm at a space
                // if so:   
                //  replace space with '%20'
                // else:
                //  move to next character
                if (myStr[i] == ' ') {
                    for (int j = (myStr.Length - 1); j > i; j--) {
                        myStr[j] = myStr[j-2];
                    }
                    myStr[i] = '%';
                    myStr[i+1] = '2';
                    myStr[i+2] = '0';
                }
            }

            str = new string(myStr);
            return str.Trim();
        }

        static bool isReturningUnchangedStringIfNoSpaces()  // Sanity Check
        {
            if (string.Equals(urlify(6, "carrot"), "carrot")) {
                return true;
            }
            return false;
        }

        static bool isReturningURLifiedString() 
        {
            if (string.Equals(urlify(15, "carrot dog door      "), "carrot%20dog%20door")) {
                return true;
            }
            return false;
        }

        
    }
}
