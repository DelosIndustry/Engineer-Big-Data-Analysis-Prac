# regression_delivery_minutes 데이터 설명

배달 주문의 예상 소요 시간을 예측하는 가상 데이터이다.
실제 배달 플랫폼 데이터나 참고서 데이터를 사용하지 않고 새로 생성했다.

## 파일
- train.csv: 학습 데이터. `delivery_minutes` 포함
- test.csv: 평가 데이터. `delivery_minutes` 미포함
- sample_submission.csv: 제출 파일 형식 예시. 컬럼명 `pred`

## 주요 컬럼
- order_id: 주문 ID
- store_type: 가게 유형
- district: 배달 권역
- order_day: 주문 요일
- order_hour: 주문 시간
- distance_km: 배달 거리
- item_count: 주문 상품 수
- fragile_count: 파손 주의 상품 수
- rain_mm: 강수량. 일부 결측치 포함
- traffic_index: 교통 혼잡도. 일부 결측치 포함
- rider_available: 주변 배달 가능 라이더 수
- promotion: 프로모션 주문 여부
- request_length: 요청사항 글자 수
- is_weekend: 주말 여부
- delivery_minutes: 배달 소요 시간. train.csv에만 존재

## 권장 사용처
- 회귀 모델링
- MAE, MSE, RMSE, R² 평가
- 수치형/범주형 전처리
- 회귀 예측값 제출 연습
