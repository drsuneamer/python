# 1 모듈 불러오기
import random

# 2 숫자 통 (1~45)
nums = range(1, 46) # 45 아니고 46!!! range(n, m) : n 이상 m 미만

# 3 그 중에서 6개를 sample
lotto = random.sample(nums, 6)

# 4. 그 결과를 출력
print(lotto)

# sorted 사용하면 더 편함
print(sorted(lotto))

# 5개 한번에도 가능
for i in range(5):
    lotto = random.sample(nums, 6)
    print(sorted(lotto))

# 한줄로도 가능
print(random.sample(range(1, 46), 6))