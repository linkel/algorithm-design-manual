# Bin Packing Problem

# Given n metal objects weighing between 0 and 1 kilograms, we 
# want to find the smallest number of bins that can hold the n objects,
# where every bin can hold at most 1 kg. 

o = [0.5, 0.7, 0.3, 0.5, 0.7, 0.3, 0.8]

# input: the n weights
# output: the number of bins used

def test_o():
    assert best_fit(o) == 2


# Okay in my head, what's gonna happen is
# I have a linked list that I keep sorted...
# I start with one node with space 1.0 and stick items in it
# when it won't fit I make another node and put that in front.
# After each insertion of items into a node I update the location of it
# based on how much space it has remaining...

# 
def best_fit(arr):
    full_bins = 0
    sorted_spaces = []
    for i in range(len(arr)):
        wt = arr[i]
        if len(sorted_spaces) == 0:
            sorted_spaces.append(1.0) # add a new bin
        j = 0
        while sorted_spaces[j] != 1.0 and j < len(sorted_spaces):
            
            j += 1

# Gah, I feel like I need to go through the sort until I hit the value
# that is too small (so it isn't minimizing the space since it won't fit)
# and back up if there's a value there and use that bin.
# then when inserting into that bin, we need to remove it from the array location
# and then slap it in its new place. 

def bf(arr):
    res = 0
    bin_remain = len(arr)*[0]
    # can only be max len(arr) bins, after all
    for i in range(len(arr)):
        mn = 1.0 + 0.1 # a min that is bigger than 1.0
        b_idx = 0 # best bin index

        for j in range(res):
            if bin_remain[j] >= arr[i] and bin_remain[j] - arr[i] < mn:
                b_idx = j
                mn = bin_remain[j] - arr[i]

        if mn == 1.0 + 0.1:
            bin_remain[res] = 1.0 - arr[i]
            res += 1
        else:
            bin_remain[b_idx] -= arr[i]
    return res 

print(bf(o))

# Okay

# We need to iterate through all items in the item array given. This is fact.
# Then we want to check up to "res" (num of bins instantiated so far), and in this loop we will 
# just find the minnest. So we will see if a spot in the bins remaining is bigger or equal to the item in the array 
# that we're looking at. And if subtracting the remaining space and the item results in something smaller than the current min
# then we definitely set it to the min and save the index that it happened at. 

# Now we do the bin filling. If min hasn't changed we know we need a new bin. New bin at index res (since it starts at 0)
# is going to be 1 - array item. 
# Result can now increment. We added a bin. 

# Otherwise we want the bin remaining's best index that we found, the minnest. And we subtract array item from it. 

# Finally we return the result. 

# For the worst fit bin heuristic, it's similar but reversed. In that case we would find the max. 

def worst_bin(arr):
    res = 0
    bin_remaining = [0] * len(arr)
    for i in range(len(arr)):
        mx = -0.1
        worst_fit_index = 0

        for j in range(res):
            if bin_remaining[j] >= arr[i] and bin_remaining[j] - arr[i] > mx:
                worst_fit_index = j
                mx = bin_remaining[j] - arr[i]

        if mx == -0.1:
            bin_remaining[res] = 1.0 - arr[i]
            res += 1
        else:
            bin_remaining[worst_fit_index] -= arr[i]

    return res

print(worst_bin(o))