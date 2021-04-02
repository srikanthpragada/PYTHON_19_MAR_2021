# Create a string that contains common chars between two strings
st1 = "How are you"
st2 = "How do you do"

common_chars = []
for c in st1:
    if c in st2 and c not in common_chars:
        common_chars.append(c)

print("".join(common_chars))

