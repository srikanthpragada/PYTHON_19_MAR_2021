st = "10,ab1c,30,5,2,xyz,pqr"

nums = filter(str.isdigit, st.split(","))
# nums = map(int, parts)
for n in sorted(nums, key=int):
    print(n)
