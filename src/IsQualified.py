
# coding: utf-8

# # 자격판별요건 프로세스

def is_qualified():
    size = ""
    print("1. 반려동물을 해외입양 하기를  원하거나 한국에 거주하는 외국인인가요?(환경)")
    print("1) O      2) X\n")
    a1 = input()
    if(a1 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("""\n\n2. “알러지 약을 복용할 경우 증상을 완화할 수는 있습니다. 
    하지만 장기적으로 복용하며 함께 지내는 것은 또 다른 문제입니다. 이에 대해 충분히 고려해보셨나요?\n
    (e.g 재채기, 기침, 콧물, 코막힘, 눈 가려움증, 충혈, 피부 발진, 두드러기, 호흡곤란, 가슴, 답답함, 천명 (호흡 시 쌕쌕거림) 등)
    """)
    print("1) O      2) X\n")
    a2 = input()
    if(a2 == '2'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n3. 강아지가 혼자 있어야 하는 시간이 8시간 이상이에요.")
    print("1) O      2) X\n")
    a3 = input()
    if(a3 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n4. 3세 미만의 자녀가 있어요.")
    print("1) O      2) X\n")
    a4 = input()
    if(a4 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n5. 반려동물을 기를 곳이 다음 중 하나에 해당하나요? ")
    print("""
    1) 공장/회사/군부대 등 사람들의 이동이 많은 곳(환경)\n
    2) 농장과 식당, 사무실 등 영업장(환경)\n
    3) 양로원,고아원과 같은 복지 시설(환경)\n
    4) 위 어느 선지에도 해당하지 않음\n
    """)
    a5 = input()
    if(a5 == '1' or a5 == '2' or a5 == '3'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n6. 반려동물 입양에 대한 동거인(가족) 간 의견이 합치되었나요? 미성년자의 경우 부모님께서 동의하셨나요?")
    print("1) O      2) X\n")
    a6 = input()
    if(a6 == '2'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n7. 본인 혹은 동거인이 우울증 등 정신 질환이 있나요?")
    print("1) O      2) X\n")
    a7 = input()
    if(a7 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n8. 반려 동물을 키우다 중간에 포기한 경우가 2 번 이상인가요?(경험)")
    print("1) O      2) X\n")
    a8 = input()
    if(a8 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size

    print("\n\n9. 3인이상의 가족이 실평수 10평이하에 거주중인가요?")
    print("1) O      2) X\n")
    a9 = input()
    a9_1 = -1
    if(a9 == '1'):
        print("당신은 현재 강아지를 키울 여건이 되지 않습니다. 충분히 준비된 후 다시 생각해보세요 :)")
        return size
    
    elif(a9 == "2"):
        print("\n\n9-1. 주거 형태가 어떻게 되나요?")
        print("1) 단독주택      2) 다가구주택(오피스텔/아파트 등)      3) 기타\n")
        a9_1 = input()


    if(a9_1 == '1'): # 대형견 이하 
        print("\n\n10. 반려동물 생활비에 고정적으로 지출 가능한 한달 비용은?")
        print("1) 5만원 이하    2) 5~13만원    3) 13만원~18만원    4)18만원 이상\n")
        a10 = input()

    elif(a9_1 == '2'): # 소형견
        print("\n\n10. 반려동물 생활에 고정적으로 지출 가능한 한달 비용은?")
        print("1) 5만원 이하    2) 5~13만원\n")
        a10 = input()
    
    elif(a9_1 == '3'): # 중형견 이하
        print("\n\n10. 반려동물 생활에 고정적으로 지출 가능한 한달 비용은?")
        print("1) 5만원 이하    2) 5~13만원    3) 13만원~18만원\n\n")
        a10 = input()
        

    # 10번 문항
    if(a10 == '2'):
        print("소형견")
        size = "S"
    elif(a10 == '3'):
        print("중형견, 소형견")
        size = "M"
    elif(a10 == '4'):
        print("대형견, 중형견, 소형견")
        size = "L"
        
    return size


# # 선호도 프로세스
def preference():
    features = ["size","grooming frequency", "shedding", "energy", "trainability"] 

    # size
    print("\n\n1. 당신은 어느 크기의 견종을 선호하나요?")
    print("1) 소형/10KG 미만    2) 중형/25KG 미만    3) 대형/25KG 이상\n")
    a1 = input()
    if(a1 == '1'):
        features[0] = "S"
    elif(a1 == '2'):
        features[0] = "M"
    elif(a1 == '3'):
        features[0] = "L"


    # grooming frequency
    print("\n\n2. 반려견의 털 손질은 몇 번이 적당하다고 생각하십니까?")
    print("1) 가끔 목욕할 때 2) 매주 한 번 브러싱 3) 주 2-3회 브러싱 4) 매일 브러싱 5) 아주 전문적으로 매일 \n")
    a2 = input()
    if(a2 == '1'):
        features[1] = 1
    elif(a2 == '2'):
        features[1] = 2
    elif(a2 == '3'):
        features[1] = 3
    elif(a2 == '4'):
        features[1] = 4
    elif(a2 == '5'):
        features[1] = 5

        
    # shedding
    print("\n\n3. 당신의 미래의 반려견의 털갈이 주기에 대한 수용 수준은 어느정도입니까?")
    print("1) 드물게 2) 때때로 3) 계절마다 4) 정기적으로 5) 자주\n")
    a3 = input()
    if(a3 == '1'):
        features[2] = 1
    elif(a3 == '2'):
        features[2] = 2
    elif(a3 == '3'):
        features[2] = 3
    elif(a3 == '4'):
        features[2] = 4
    elif(a3 == '5'):
        features[2] = 5
        
    # energy
    print("""\n\n4. 반려견과의 산책은 보호자의 의무이자 행복입니다.
          얼마나 활동적인 반려견과 함께하고 싶은가요?""")
    print("1) 대체로 누워있는    2) 차분한    3) 보통의   4) 에너제틱한   5) 엄청난 활동량을 자랑하는 \n")
    a4 = input()
    if(a4 == '1'):
        features[3] = 1
    elif(a4 == '2'):
        features[3] = 2
    elif(a4 == '3'):
        features[3] = 3
    elif(a4 == '4'):
        features[3] = 4
    elif(a4 == '5'):
        features[3] = 5


    # trainability
    print("\n\n5. 당신이 반려견을 트레이닝 할 때 최대한으로 다룰 수 있는 반려견의 성격은?")
    print("1) 고집이 있는 반려견 2) 독립적인 반려견 3) 순응하는 반려견 4) 트레이닝이 쉬운 반려견 5) 무엇이든 할 준비가 된 반려견\n")
    a5 = input()
    if(a5 == '5'):
        features[4] = 1
    elif(a5 == '4'):
        features[4] = 2
    elif(a5 == '3'):
        features[4] = 3
    elif(a5 == '2'):
        features[4] = 4
    elif(a5 == '1'):
        features[4] = 5


    return features

        
