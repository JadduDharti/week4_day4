# Sum of Pairs
# Given a list of integers and a single sum value, return the 
#first two values (parse from the left please) in order of appearance 
#that add up to form the sum.

# If there are two or more pairs with the required sum,
# the pair whose second element has the smallest index is the solution.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]



def sum_pairs(ints, s):
    indices = []
    for i in ints:
        if (s-i) in ints[ints.index(i)+1:]:
            # print(ints.index(i))
            # print(ints[ints.index(i)+1:])
            # print(i,s-i)
            indices.append([ints.index(i),ints[ints.index(i)+1:].index(s-i)+len(ints[:ints.index(i)])+1])
    if(len(indices) == 0):
        return None
    # print(indices)
    indices.sort(key=lambda x: x[1])
    #print(indices)
    return [ints[indices[0][0]], ints[indices[0][1]]]

print(sum_pairs([11, 3, 7, 5], 10))
