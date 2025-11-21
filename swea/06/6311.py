# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수_4

# map(함수, 반복 가능한 객체)
# lambda : 익명 함수
# lambda 내부에서는 elif 키워드 작성 불가능

word = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
word_list = map(lambda ch: 4 if ch == "A" else 3 if ch == "B" else 2 if ch == "C" else 1, word)

print(sum(word_list))