#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

"""
Sources:
    https://www.geeksforgeeks.org/quick-sort/
    https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill
"""
def quicksort(numbers_in_a_list):
    less = [] #Empty sublsits to sort integers less than or greater than pivot item.
    greater = []
    if len(numbers_in_a_list) <= 1: #Base case occurs here when sublists are either 1 or 0.
        return numbers_in_a_list
    else:
        pivot = numbers_in_a_list.pop() #Removes element from list.
    for number in numbers_in_a_list: #Appends number into correct corresponding sublist.
        if number < pivot:
            less.append(number)
        else:
            greater.append(number)
    return quicksort(less) + [pivot] + quicksort(greater) #Returns one large list containing all elements from both sublists including pivot in the middle.


def main():
    with open("numbers.txt") as fin: #Opens numbers.txt file, takes in as string, converts string to list.
        string_list = fin.read()
        empty_list = string_list.split(",")
    sorted_list = quicksort(empty_list) #Creates new list, sorted_list, by running empty_list through quicksort function.
    with open("sorted.txt", "w") as fout: #Creates new file sorted.txt and writes in sorted_list.
        fout.write(str(sorted_list))
    return quicksort(sorted_list)

if __name__ == "__main__":
    main()
