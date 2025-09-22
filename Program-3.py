def generate_series(a: int):
    if a % 2 == 0:
        a -= 1     
    series = []
    for i in range(1, a + 1, 2):  
        series.append(i)
    return series
a = int(input("Enter a number: "))
result = generate_series(a)
print("Series:", ", ".join(map(str, result)))