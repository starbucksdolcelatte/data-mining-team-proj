
# coding: utf-8

# # 자격판별요건 프로세스



# 1. 반려 동물 생활비
print("반려동물 생활에 고정적으로 지출 가능한 한달 비용은?")
print("1) 5만원 이하    2) 5~13만원    3) 13만원~18만원    4)18만원 이상 ")
a1 = input()

#2. 환경
print("2. 3인이상의 가족이 실평수 10평이하에 거주중인가요?")
print("1) O      2) X")
a2 = input()
a2_1 = -1
if(a2 == "2"):
    print("2-1. 주거 형태가 어떻게 되나요?")
    print("1) 단독주택      2) 다가구주택(오피스텔/아파트 등)      3) 기타")
    a2_1 = input()

print("3. 강아지가 혼자 있어야 하는 시간이 8시간 이상이에요.")
print("1) O      2) X")
a3 = input()

print("4. 3세 미만의 자녀가 있어요.")
print("1) O      2) X")
a4 = input()

print("5. 반려동물을 기를 곳이 다음 중 하나에 해당하시나요? ")
print("""
1) 공장/회사/군부대 등 사람들의 이동이 많은 곳(환경)\n
2) 농장과 식당, 사무실 등 영업장(환경)\n
3) 양로원,고아원과 같은 복지 시설(환경)\n
4) 위 어느 선지에도 해당하지 않음
""")
a5 = input()

print("6. 반려동물과 함께하는 것에 대한 가족 간 의견이 합치되었나요? 미성년자의 경우 부모님께서 동의하셨나요?")
print("1) O      2) X")
a6 = input()

print("7. 동거인이 우울증 등 정신 질환이 있나요?")
print("1) O      2) X")
a7 = input()

print("8. 반려 동물을 키우다 중간에 포기한 경우가 2 번 이상인가요?(경험)")
print("1) O      2) X")
a8 = input()

print("""9. “알러지 약을 복용할 경우 증상을 완화할 수는 있습니다. 
하지만 장기적으로 복용하며 함께 지내는 것은 또 다른 문제입니다. 이에 대해 충분히 고려해보셨나요?\n
(e.g 재채기, 기침, 콧물, 코막힘, 눈 가려움증, 충혈, 피부 발진, 두드러기, 호흡곤란, 가슴, 답답함, 천명 (호흡 시 쌕쌕거림) 등)
""")
print("1) O      2) X")
a9 = input()

print("10. 외국으로 이민을 원하거나 한국에 거주하는 외국인인가요?(환경)")
print("1) O      2) X")
a10 = input()

print("11. 당신과 동거인은 애견의 털날림의 어느정도까지 인내할 수 있나요?")
print("""
1) 절대 인내할 수 없다\n
2) 다소 참을 수 없는 편이다\n
3) 어느 정도 참을 수 있다\n
4) 다소 신경쓰지 않는다\n
5) 전혀 상관없다
""")
a11 = input()




if(a2 == '1' or a3 == '1' or a4 == '1' or a5 != '4' or a6 == '2' or a7 == '1' or a8 == '1' or a9 == '2' or a10 == '1'):
    print("당신은 강아지를 키울 자격이 없습니다ㅜㅜ")

# 1번 문항
if(a1 == '1'):
    print("소형견")
elif(a1 == '2'):
    print("소형견")
elif(a1 == '3'):
    print("중형견")
elif(a1 == '4'):
    print("대형견")
    
# 2-1번 문항
if(a2_1 == '1'):
    print("소, 중, 대형견")
elif(a2_1 == '2'):
    print("소형견")
elif(a2_1 == '3'):
    print("소, 중형견")

# 11번 문항
if(a11 == '1'):
    print("Shedding 0~20% 견종 추천")
elif(a11 == '2'):
    print("Shedding 20~40% 견종 추천")
elif(a11 == '3'):
    print("Shedding 40~60% 견종 추천")
elif(a11 == '4'):
    print("Shedding 60~80% 견종 추천")
elif(a11 == '5'):
    print("Shedding 80~100% 견종 추천")
