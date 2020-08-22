#-----------PROBLEM---------------
#Given a target amount n and a list (array) of distinct coin values, 
#what's the fewest coins needed to make the change amount.
#--------------------------------



def rec_coin(target,coins):
    min_coins = target
    
    if target in coins:
        return 1
    
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i,coins) #add a count coin and subtract from the target
            if num_coins < min_coins:
                min_coins = num_coins    
    return min_coins

def rec_coin_dynam(target,coins,known_results):

    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
                
    return min_coins


from nose.tools import assert_equal
class TestCoinChange(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins,[0]*(46)),3)
        assert_equal(solution(23,coins,[0]*(24)),5)
        #assert_equal(solution(74,coins),[0]*(75),8)
        print ('Passed all tests.')
        
test = TestCoinChange()
test.check(rec_coin_dynam)