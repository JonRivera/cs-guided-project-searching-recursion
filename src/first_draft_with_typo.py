"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""


# Understand
# Find the first draft corresponds to the typo
# We are given a lists numberrs that represent documents
# We are given some function containsTypo() which checks if the current draft has a type
# Questions:
# Do we have order?what is the length of the current data ? What data structure are we given?
# There is order b/c each draft that follows the present one depends on the previous one in chronological order
# Plan:
# what type of problem is this? ---> searching problem
# what techniques do I know that can help solve this problem?
# We can use a binary search which help me split the search for this document by creating two search spaces
# How am I going to imlplement this algorithim?

# Execution
# Start at element 1, and go up to element n


def firstDraftWithTypo(n):
    left = 1
    right = n  # this is the nth draft

    while left < right:  # this only holds if there is a middle point btw left and right
        # figure out out the midpoint of the range 1 .. n 
        mid = left + (right - left) // 2
        # check if the midpoint draft has a typo 
        # if it has a typo
        if containsTypo(mid):
            # this is either the first draft typo, or 
            # it happened earlier 
            # so we need check the earlier drafts to 
            # determine where the first typo is 
            right = mid
        # it doesn't have a typo 
        else:
            # the typo must have happened in a later draft 
            # so we don't have to consider any of the earlier drafts
            left = mid + 1  # this step also helps us narrow the draft with the typo

    return left  # happens when left == to right draft ----> which mean this current right is the draft with the typo

# def firstDraftWithTypo(n):
#     # Your code here
#     # iterate through from 1 to n 
#     for i in range(1, n + 1): # O(n)
#         # if containsTypo(draft)
#         if containsTypo(i): # O(1)
#             # return draft 
#             return i
#     # return -1
#     return -1
