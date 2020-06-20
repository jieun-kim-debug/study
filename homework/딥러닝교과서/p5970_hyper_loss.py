# 손실 함수
# 학습시 모델의 출력과 지도 데이터의 차이를 평가하는 함수
# 제곱오차와 교차 엔트로피 오차가 사용
# 이 손실 함수를 최소화 하도록 오차역전파법으로 각 층의 가중치가 갱신
# 손실함수는 가중치를 갱신할 때 중요한 역할을 하므로 적절한 것을 선택

# 제곱오차
# 연속값 평가가 뛰어나므로 주로 회귀 모델의 오차 함수로 사용
# (실제값-예측값)**2 모두 합친 제곱오차
# 회귀에 적합하며 최소치 부근에서 천천히 갱신되므로 학습이 수렴하기 쉽다

# 교차 엔트로피 오차
# 이항 분류의 평가에 특화
# 교차 엔트로피 오차는 |예측값-실제값|이 클 때 매우 큰 값을 반환하고 반대로 작을 때 0에 가까운 값을 취한다
# 분류 학습에서 예측값과 실제값은 가까울수록 좋으므로 유용
# 교차 엔트로피 오차는 0~1 사이에 있는 두 숫자의 차이를 평가하는 합리적인 함수
