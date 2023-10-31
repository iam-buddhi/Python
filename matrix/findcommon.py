# Function to find all common elements present in every row of a given matrix
def findCommonElements(mat):

	# base case
	if not mat or not len(mat):
		return set()

	# `M × N` matrix
	M = len(mat)
	N = len(mat[0])

	# Create an empty dictionary
	d = {}

	# Insert all elements of the first row into the dictionary
	# with their value set as 1
	for c in range(N):
		d[mat[0][c]] = 1

	# Do for remaining rows
	for r in range(1, M):
		for c in range(N):
			# Get the current element
			curr = mat[r][c]

			# if the current element is present in the dictionary and its value
			# is the same as the row index, increment its value by 1.
			# This check also handles duplicate entries in the same row.
			if curr in d and d[curr] == r:
				d[curr] = r + 1

	# Iterate over each entry in the dictionary and print keys having
	# their value equal to `M` (number of rows in the matrix)
	print('The common elements are:', [k for k in d.keys() if d.get(k) == M])


if __name__ == '__main__':

	mat = [
		[7, 1, 3, 5, 3, 6],
		[2, 3, 6, 1, 1, 6],
		[6, 1, 7, 2, 1, 4],
		[6, 6, 7, 1, 3, 3],
		[5, 5, 6, 1, 5, 4],
		[3, 5, 6, 2, 7, 1],
		[4, 1, 4, 3, 6, 4],
		[4, 6, 1, 7, 4, 3]
	]

	findCommonElements(mat)
