def count_vowel(str):
    vowel = 0
    for c in str:
        if c in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
            vowel = vowel + 1    
    print(f"สระในภาษอังกฤษในประโยคที่พิมมา มี {vowel} ตัว "  )


n = str(input("กรอกคำ>>"))
count_vowel(n)
