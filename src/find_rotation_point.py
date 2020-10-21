"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""


def find_rotation_point(surnames):
    left = 0
    right = len(surnames) - 1
    first = surnames[0]

    while left < right:
        mid = left + (right - left) // 2

        if surnames[mid] >= first:  # [4,5,6,7,1,2,3], len == 7, middle  == 3, left = 0, right =6 --->left = 4, right = 6 mid == 5
                                    # Rotation == 4 index------- If this case breaks then it means it broke at the start of the other order
            # the left side is entirely sorted
            # go right 
            left = mid
        else:
            # the right side is entirely sorted 
            # go left 
            right = mid # the pivot of before right order starts

            # have left and right gotten right next to one another?
        if left + 1 == right:#  the right belongs to the same order as the left ---> belongs to the left order this where the rotation took place
            return right

    return -1


surnames = [
    'arthur',
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
]

print(find_rotation_point(surnames))
