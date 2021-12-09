

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

my_list = [1, 4, 7, 'as', 'se']

def flat_generator(list_1):
	for n in list_1:
		for m in n:
			total = m
			yield total

class FlatIterator:

	def __init__(self, lists):
		self.list = lists


	def __iter__(self):
		self.cursor = -1
		self.t = -1

		return self

	def __next__(self):
		self.cursor += 1

		if self.cursor == len(self.list):
			raise StopIteration
		list_1 = self.list[self.cursor]
		# print(list_1)
		for self.t in list_1:
			final = self.t

			return final




for item in FlatIterator(nested_list):
	print(item)


# for item in flat_generator(nested_list):
# 	print(item)