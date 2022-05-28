# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    find_anagrams("hello", "check")
    find_anagrams("below", "elbow")
    if (sorted(word) == sorted(anagram)):
        print("They are anagrams")
    return True
    else:
        print("They are not anagram")
        return False