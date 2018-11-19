using System;

namespace IsUnique
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(IsUniqueReturnsTrueWhenItShould());
            Console.WriteLine(IsUniqueReturnsFalseWhenItShould());
        }

        static bool IsUnique(String s) 
        {
            char[] str = s.ToCharArray();
            Array.Sort(str);
            for (int i = 0; i < (str.Length - 1); i++) {
                if (str[i] == str[i+1]) {
                    return false;
                }
            }

            return true;
        }

        static bool IsUniqueReturnsTrueWhenItShould() {
            if (IsUnique("orange") == true) {
                return true;
            }

            return false;
        }

        static bool IsUniqueReturnsFalseWhenItShould() {
            if (IsUnique("hello") == false) {
                return true;
            }

            return false;
        }
    }
}
