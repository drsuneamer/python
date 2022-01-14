# 1. 모듈 불러오기
import random

# 2. 점심 메뉴 리스트 만들기
Lunch = ['서브웨이', '치킨', '아이스크림', '스테이크']
Dinner = ['샐러드', '파스타']
Meal = [Lunch, Dinner]

# 3. 하나를 랜덤으로(random) 선택하여(choice) 저장한다.
today_menu = random.choice(Lunch)

# 4. 출력한다.
print(today_menu)
# or
print(random.choice(Lunch))


# print(Lunch[0])
# print(type(Lunch))


