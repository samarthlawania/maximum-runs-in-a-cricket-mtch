O = int(input("Enter the number of overs bowled"))
R = ((O * 6) - (O - 1)) * 6
r = (O - 1) * 3
I = R + r
print(f"The highest score one player can score is { I }")
