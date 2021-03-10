count = 0
for num in range(10):
    if num % 2 == 0 and num != 0:
        print(num)
        count += 1
print(f"hurray {count} counted")
