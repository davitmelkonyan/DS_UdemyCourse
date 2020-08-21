
def largest_cont_sum(arr):
    if len(arr)==0: 
        return 0
    max_sum=current_sum=arr[0] 
    for num in arr[1:]: #skip the first element becasuse assigned above
        current_sum=max(current_sum+num, num) #higher of the two, num can be negative 
        max_sum=max(current_sum, max_sum) # the higher between the currentSum and the current max
    return max_sum 

#print(largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
#print(largest_cont_sum([1,2,-1,3,4,-1]))

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(largest_cont_sum)
