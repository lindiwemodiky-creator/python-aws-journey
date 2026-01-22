# Loop Practice - Understanding FOR loops
print("EXAMPLE 1: Basic Counting")
# range(5) creates numbers: 0, 1, 2, 3, 4
for number in range(5):
    print(number)
print()
print("EXAMPLE 2: Counting 1-20")
# range(1, 20) creates: 1, 2, 3, ... 20
# Start at 1, stop BEFORE 11
for number in range(1, 21):
    print(number)
print()
print("EXAMPLE 3: Countdown")
# range(10, 0, -1) counts backwards
# Start at 10, stop before 0, step by -1
for number in range(10, 0, -1):
    print(number)
    print("Blast off! 🚀")
print()
print("EXAMPLE 4: Multiples of 5")
# range(5, 21, 5) means: start 5, stop before 21, step by 5
for number in range(5, 21, 5):
    print(number)
print()
print("EXAMPLE 5:Repeating the text")
# Loop runs 5 times
for i in range(5):
    print("I am learning python!")
print()
print("EXAMPLE 6: Using Loop Variable")
for day in range(1, 8):
    print(f"Week {day} of my coding journey")
print()
print("WHILE LOOP EXAMPLE")
#  While loop: repeats AS LONG condition is true
count = 1
while count < 5:
    print(f"Count is: {count}")
    count = count + 1  # Increase by 1 each time
    print("Loop finished!")
    # WARNING: Be careful with while loops!
    # If condition is ALWAYS true, loop never stops (infinite loop)
    # Always make sure the condition eventually becomes false
