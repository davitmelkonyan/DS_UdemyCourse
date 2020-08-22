#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
# For this problem, you can falsely "compress" strings of single or double letters. 
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
#--------------------------------------------------
def my_compress(s):
    ans = ""
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s + "1"

    last_letter = s[0]
    letter_count = 1

    i = 1 #start from second elem
    l = len(s)
    while i < l:
        if s[i] == s[i - 1]: 
            letter_count+=1
        else:
            ans += s[i-1]+str(letter_count)
            letter_count = 1
        i+=1
    ans += s[i - 1] + str(letter_count)
    return ans


from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(my_compress)
    
    