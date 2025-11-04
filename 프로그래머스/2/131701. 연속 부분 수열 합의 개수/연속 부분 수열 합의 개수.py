def solution(elements):
    s = set()
    s.add(sum(elements))
    for size in range(1, len(elements)):
        window = sum(elements[:size])
        idx = size
        for _ in range(len(elements)):
            window += elements[idx]
            window -= elements[idx - size]
            s.add(window)
            idx = (idx + 1) % len(elements)
    return len(s)