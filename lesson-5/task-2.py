word = input("Введите слово из маленьких латинских букв: ").strip().lower()

vowels = {"a", "e", "i", "o", "u"}

vowel_count = sum(1 for ch in word if ch in vowels)
consonant_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)

each = {v: word.count(v) for v in vowels}

print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")
print(f"a: {each['a']}, e: {each['e']}, i: {each['i']}, o: {each['o']}, u: {each['u']}")

if any(each[v] == 0 for v in vowels):
    print(False)
