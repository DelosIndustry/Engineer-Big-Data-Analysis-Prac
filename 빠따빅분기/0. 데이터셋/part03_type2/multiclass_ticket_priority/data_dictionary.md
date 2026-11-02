# multiclass_ticket_priority 데이터 설명

고객 문의 티켓의 우선 처리 수준을 예측하는 가상 데이터이다.
실제 고객센터 데이터나 참고서 데이터를 사용하지 않고 새로 생성했다.

## 파일
- train.csv: 학습 데이터. `priority_level` 포함
- test.csv: 평가 데이터. `priority_level` 미포함
- sample_submission.csv: 제출 파일 형식 예시. 컬럼명 `pred`

## target
- priority_level = 0: 낮음
- priority_level = 1: 보통
- priority_level = 2: 높음

## 주요 컬럼
- ticket_id: 문의 ID
- channel: 문의 채널
- product_area: 문의 분야
- user_plan: 이용 요금제
- browser: 사용 브라우저. 일부 결측치 포함
- signup_days: 가입 후 지난 일수
- open_hour: 문의 접수 시간
- message_length: 문의 글자 수
- previous_tickets: 이전 문의 수
- has_screenshot: 화면 캡처 첨부 여부
- urgency_words: 긴급 표현 개수
- sentiment_score: 문장 분위기 점수. 일부 결측치 포함
- weekend_open: 주말 접수 여부
- file_count: 첨부 파일 수

## 권장 사용처
- 다중 분류
- `predict()` 연습
- Accuracy, F1-score, Macro F1 평가
- 범주형 인코딩
- train/test 더미 컬럼 불일치 처리
