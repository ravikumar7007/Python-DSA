def check_balance(s: str):
    arr = []  
    for i, ch in enumerate(s):
        if ch in "([{":
            arr.append((ch, i + 1)) 
        elif ch in ")]}":
            if not arr:
                return i + 1 
            last_bracket, last_pos = arr.pop()
            if (
                (ch == ")" and last_bracket != "(")
                or (ch == "]" and last_bracket != "[")
                or (ch == "}" and last_bracket != "{")
            ):
                return i + 1  
    if not arr:
        return "Success"
    else:
        return arr[0][1]


if __name__ == "__main__":
    s = input().strip()
    result = check_balance(s)
    print(result)
