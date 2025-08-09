def solution(brown, yellow):
    size = brown + yellow
    for w in range(1, int(size ** 0.5) + 2):
        if size % w: continue
        h = size // w
        if (w-2) * (h-2) == yellow:
            return [h, w]
