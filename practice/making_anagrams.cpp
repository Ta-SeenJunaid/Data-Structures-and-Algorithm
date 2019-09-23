/*
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,
and , that may or may not be of the same length, determine the minimum number of character deletions required to make and

anagrams. Any characters can be deleted from either of the strings.

For example, if
and , we can delete from string and from string so that both remaining strings are and

which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

    a: a string
    b: a string

Input Format

The first line contains a single string,
.
The second line contains a single string,

.

Constraints

The strings and

    consist of lowercase English alphabetic letters ascii[a-z].

Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc

Sample Output

4

Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

    Remove d and e from cde to get c.
    Remove a and b from abc to get c.

We must delete
characters to make both strings anagrams, so we print on a new line.


*/



#include <bits/stdc++.h>
using namespace std;


int make_anagram(string s1, string s2){

    int a[28], b[28], count=0;
    
    memset(a, 0, sizeof(int)*28);
    memset(b, 0, sizeof(int)*28);

    for(int i=0; i < s1.size(); i++){
            a[s1[i] - 'a']++;

    }

    for(int i=0; i < s2.size(); i++){
            b[s2[i] - 'a']++;

    }

    for(int i= 0; i < 26; i++){
        if(a[i] != b[i]){
            int d = abs(a[i]-b[i]);
            count += d;
        }
    }

    return count;

}

int main()
{
    int a[28],b[28], count = 0;
    string s1, s2;
    cout << "Input 1st string:";
    cin >> s1;

    cout << "Input 2nd string:";
    cin >> s2;

    

    cout << make_anagram(s1, s2) << endl;    

    return 0;
}
