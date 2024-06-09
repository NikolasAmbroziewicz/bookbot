def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)

  generate_report(book_path, num_words, chars_dict)

def get_num_words(text):
  words = text.strip().split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def generate_report(book_name, num_words, chars_dict):
  print(f'--- Begin report of #{book_name} ---')
  print(f'#{num_words} words found in the document')

  for key in chars_dict:
    print(f'The "{key}" character was found {chars_dict[key]} times')

main()