
def mergesort (nums):
	if len (nums) <= 1:
		return nums
	else:
		mid = len (nums) // 2
		left = nums [0 : mid]
		right = nums [mid : len (nums) ]
		left = mergesort (left)
		right = mergesort (right)

		if left [-1] > right [0]:
			return merge (left, right)					
		else:
			return left + right

def merge (left, right):
	erg = []
		
	while len( left ) > 0 and len( right ) > 0:
		if left [0] <= right [0]:
			erg.append ( left [0])
			left = left [1:]
		else:
			erg.append ( right [0])
			right = right [1:]
	if len (left) > 0: # append the rest
		erg += left
	else:
		erg += right
	return erg




def main ():

	nums = [1,3,6,33,43,41,4,14,134,34,34,1,41,4]
	mid = len (nums) // 2
	left = nums [0 : mid+1]
	right = nums [mid+1 : len (nums) ]

	print (left)
	print (right)


	print ("Presort ist: ", nums)
	print ("Postsort ist: ", mergesort (nums) )

main ()