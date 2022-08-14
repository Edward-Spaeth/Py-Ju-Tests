import random

def quicksort (nums, p, r):

    if p < r:
        j = hoare_partition (nums, p, r)
        quicksort (nums, p, j)
        quicksort (nums, j+1, r)
    return nums


def hoare_partition (nums, p, r):

    pivot = nums [p]
    i = p-1
    j = r+1

    while True:

        while True:
            i += 1
            if (nums [i] >= pivot):
                break

        while True:
            j -= 1
            if (nums [j] <= pivot):
                break
        if i < j:
            nums [i], nums [j] = nums [j], nums [i]
        else:
            break

    return j

def randomize (nums, size):

    for i in range (0, size):
        nums.append (random.randint (0,87))

def main ():

    nums = []

    size = 10

    randomize (nums, size)


    print ("Array Presort:", nums)

    quicksort (nums, 0, len (nums)-1)

    print ("Array Postsort:", nums)




if __name__ == "__main__":
    main ()