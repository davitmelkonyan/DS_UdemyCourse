#Given a string,determine if it is compreised of all unique characters. 
# For example, the string 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters and should return false.
#--------------------------------------------------------------------------

def unique_char1(s):
    return len(set(s)) == len(s) #set has only unique chars

def unique_char2(s):
    i = 0
    l = len(s)
    lettersInS = []
    while i<l:
        if s[i] in lettersInS:
            return False
        else:
            lettersInS.append(s[i])
        i+=1
    return True


from nose.tools import assert_equal
class Test(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
t = Test()
t.test(unique_char1)
t.test(unique_char2)
