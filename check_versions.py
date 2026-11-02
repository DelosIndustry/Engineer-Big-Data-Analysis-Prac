# 공식 체험환경 가이드(K-DATA, 2025.06)에 수록된 패키지 확인 코드
# 시험장/체험환경에서 그대로 실행해 로컬 bigdata 환경과 비교하세요.
import sys
print("python", sys.version)

import pkg_resources
import pandas
pandas.set_option('display.max_rows', None)
OutputDataSet = pandas.DataFrame(sorted(
    [(i.key, i.version) for i in pkg_resources.working_set]))
print(OutputDataSet)

print("\n=== 핵심 패키지 ===")
import numpy, scipy, sklearn, statsmodels, xgboost, lightgbm
for m in (numpy, pandas, scipy, sklearn, statsmodels, xgboost, lightgbm):
    print(f"{m.__name__:<12} {m.__version__}")
