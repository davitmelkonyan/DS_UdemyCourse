#p1: Recursive Sum
def rec_sum(n):
    if(n==0):
        return 0
    else:
        return n + rec_sum(n-1)
    
print(rec_sum(4))

#p2: Sum of individual digits
def sum_func(n):
    if(len(str(n))==1):
        return n
    else:
        return n%10 + sum_func(n//10)#classical division

print(sum_func(44))

#p3: Word Split
def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)
    return output
