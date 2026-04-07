# Optimization Theory (수치해석)

수치해석 강의에서 다루는 최적화 및 수치 알고리즘의 Python 구현입니다.

## 알고리즘 목록

| 파일 | 알고리즘 | 설명 |
|------|----------|------|
| `false_position.py` | 가위치법 (False Position Method) | 비선형 방정식의 근을 구하는 구간 기반 방법 |

## 실행 방법

```bash
python false_position.py
```

### 예제: 번지점프 질량 구하기

공기 저항 계수 `cd=0.25`, 시간 `t=4`초 후 속도 `v=36 m/s`를 만족하는 질량 `m`을 구합니다.

```
root    = 142.73762052020272
f(root) = 5.655427948392017e-11
ea      = 8.410873963942408e-08
iter    = 30
```

## 환경

- Python 3.x
- NumPy
