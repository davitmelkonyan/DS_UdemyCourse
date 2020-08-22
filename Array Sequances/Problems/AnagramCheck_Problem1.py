#anagram is when two strings can be written with exacts same letters (ignore spaces/capitalization)

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1)== sorted(s2)

print(anagram('clint eastwood','old west action'))
print(anagram('clint eastwood','oold west action'))

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    if len(s1)!= len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k]!=0:
            return False
    return True

print(anagram2('clint eastwood','old west action'))
print(anagram2('clint eastwood','oold west action'))