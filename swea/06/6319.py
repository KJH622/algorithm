# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_1

# 반복문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고 회문 여부를 판단하는 코드 작성하시오

def word_reverse(word):
    reversed_word = ''
    for ch in word:
        reversed_word = ch + reversed_word
    
    print(reversed_word)

    if word == reversed_word:
        print("입력하신 단어는 회문(Palindrome)입니다.")

    return reversed_word

word = input()
word_reverse(word)