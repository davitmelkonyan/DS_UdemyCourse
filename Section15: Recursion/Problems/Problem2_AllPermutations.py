from nose.tools import assert_equal
#Iterate through the initial string – e.g., ‘abc’.
#For each char, set aside that char and get a list of all permutations of the string that’s left. For example, current iteration is on 'b', find all the permutations of the string 'ac'.
#Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.
#Return the list of final results.

def permute(s):
    out = []
    if len(s) == 1:
        out = [s] 
    else:
        for i, value in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]): #skip the chosen char 
                out += [value + perm] 
    return out

class TestPerm(object):
    def test(self,solution):
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        print ('All test cases passed.')
        

t = TestPerm()
t.test(permute)