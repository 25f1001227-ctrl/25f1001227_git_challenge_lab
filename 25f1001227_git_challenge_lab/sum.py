cat > sum.py <<'PY'
def add(a, b):
    return a + b

if _name_ == "_main_":
    print("Sum of 5 and 3 is:", add(5, 3))