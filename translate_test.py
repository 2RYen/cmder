# 구글 번역기
import googletrans

translator = googletrans.Translator()
str1 = "나는 학생입니다."
str2 = "I like Movie."
result1 = translator.translate(str1, dest="en")
result2 = translator.translate(str2, dest="ko")
print(str1, "===>", result1.text)
print(str2, "===>", result2.text)