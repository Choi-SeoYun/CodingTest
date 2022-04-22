import math

def solution(w,h):
    answer = 1
    area = w*h
    return area - (w + h - math.gcd(w,h))