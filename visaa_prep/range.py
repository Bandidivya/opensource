def binary_hear(t, frequencies):
    results = []
    for freq in frequencies:
        if 67 <= freq <= 45000:
            results.append("YES")
        else:
            results.append("NO")
    return results
t = int(input())
frequencies = [int(input()) for _ in range(t)]
results = binary_hear(t, frequencies)
for result in results:
    print(result)
