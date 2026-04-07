import numpy as np


def false_position(func, xl, xu, tol=1e-4, max_iter=100):
    """가위치법(False Position Method)으로 근을 구한다.

    Args:
        func: 근을 구할 함수 f(x)
        xl: 구간 하한
        xu: 구간 상한
        tol: 상대 근사 오차 허용치 (%, 기본값 0.01%)
        max_iter: 최대 반복 횟수

    Returns:
        (root, f(root), 상대근사오차, 반복횟수) 튜플.
        부호 변화가 없으면 (None, None, None, None).
    """
    if func(xl) * func(xu) > 0:
        print("no sign change")
        return None, None, None, None

    xr = xl
    approx_error = 100.0

    for iteration in range(1, max_iter + 1):
        xr_old = xr
        fl, fu = func(xl), func(xu)

        if fl == fu:
            print("Division by zero in false position formula.")
            break

        xr = xu - fu * (xl - xu) / (fl - fu)

        if xr != 0:
            approx_error = abs((xr - xr_old) / xr) * 100

        fr = func(xr)
        if fl * fr > 0:
            xl = xr
        elif fl * fr < 0:
            xu = xr
        else:
            approx_error = 0.0

        if approx_error <= tol:
            break

    return xr, func(xr), approx_error, iteration


if __name__ == "__main__":
    g = 9.81
    cd = 0.25
    t = 4
    v_target = 36

    func = lambda m: np.sqrt(g * m / cd) * np.tanh(np.sqrt(g * cd / m) * t) - v_target

    root, fx, ea, niter = false_position(func, xl=40, xu=200)

    print(f"root    = {root}")
    print(f"f(root) = {fx}")
    print(f"ea      = {ea}")
    print(f"iter    = {niter}")
