def sort(dict):
	return dict["count"]

def print_report(word_count, letter_counts):
	print("--- Begin report of books/frankenstein.txt ---\n")
	print(f"{word_count} words found in the document.\n")
	items = []

	for key in letter_counts:
		item = {
			"letter":key,
			"count":letter_counts[key]
		}
		items.append(item)
	items.sort(reverse=True, key=sort)
	
	for item in items:
		letter = item["letter"]
		count = item["count"]
		print(f"The \'{letter}\' character was found {count} times.")
	print("--- end report ---")

def count_characters(text):
	t = text.lower()
	counts = {}
	for letter in t:
		if not letter.isalpha():
			continue
		if letter not in counts:
			counts[letter] = 0

		counts[letter] += 1

	return counts

def count_words(text):
	return len(text.split())

def main():
	word_count = 0
	letter_counts = None
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		word_count = count_words(file_contents)
		letter_counts = count_characters(file_contents)
		print_report(word_count, letter_counts)


main()

'''
{'p': 6121, 'r': 20818, 'o': 25225, ...
'''