name = input("What is your name? ").strip().title()

if "," in name:
    last, first = name.split(",")
    name = f"{first.strip()} {last.strip()}"
print(f"Hello, {name}")
