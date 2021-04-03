
st  = "How are you today?"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")
