question = "Which planet is known as the Red Planet?"
options = ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"]
answer = "B"

print(question)
for opt in options:
    print(opt)

user = input("Your answer (A/B/C/D): ").upper()

if user == answer:
    print("Correct! You won ₹1000")
else:
    print("Wrong! The correct answer is", answer)