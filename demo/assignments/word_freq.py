st = "How do you do today? How did you do yesterday?"

words = st.split(" ")
for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")
