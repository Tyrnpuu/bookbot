from stats import get_num_words, get_num_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    rel_path = "./books/frankenstein.txt"
    text = get_book_text(rel_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = sort_characters(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()