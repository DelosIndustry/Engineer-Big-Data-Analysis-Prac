# binary_learning_renewal 데이터 설명

온라인 학습 서비스의 다음 달 수강 연장 여부를 예측하는 가상 데이터이다.
실제 서비스 데이터나 참고서 데이터를 사용하지 않고 새로 생성했다.

## 파일
- train.csv: 학습 데이터. `renew_next_month` 포함
- test.csv: 평가 데이터. `renew_next_month` 미포함
- sample_submission.csv: 제출 파일 형식 예시. 컬럼명 `pred`

## 주요 컬럼
- student_id: 학습자 ID
- age_group: 연령대
- region: 거주 권역
- device_type: 주 사용 기기
- course_category: 수강 분야
- membership_months: 가입 후 개월 수
- study_minutes_week: 최근 1주 학습 시간
- completed_lessons: 완료한 강의 수
- quiz_avg_score: 퀴즈 평균 점수. 일부 결측치 포함
- assignment_rate: 과제 제출률
- late_submission_count: 지각 제출 횟수
- community_posts: 커뮤니티 글 작성 수
- coupon_used: 쿠폰 사용 여부
- last_login_days: 마지막 접속 후 지난 일수
- renew_next_month: 다음 달 연장 여부. train.csv에만 존재

## 권장 사용처
- 이진 분류
- `predict_proba()` 연습
- ROC-AUC 평가
- 범주형 인코딩
- train/test 더미 컬럼 불일치 처리
