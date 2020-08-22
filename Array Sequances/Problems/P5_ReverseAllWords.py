def rev_words1(s):
    return " ".join(reversed(s.split()))

def rev_words2(s):
    return " ".join(s.split()[::-1])   

print (rev_words2('Hi John,   are you ready to go?'))

def my_rev(s):
    words = []
    length = len(s)
    spaces = [" "]
    #splitting manualy
    i=0
    while (i<length):
        if s[i] not in spaces:#if elem is not a space
            wordStart = i
            while i<length and s[i] not in spaces:
                i+=1
            words.append(s[wordStart:i])
        i+=1
    return " ".join(reversed(words))

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(my_rev)

