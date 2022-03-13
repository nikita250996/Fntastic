from collections import Counter


def convert(data: str) -> str:
    data = data.casefold()
    counter = Counter(data)
    result = ""
    for char in data:
        result += "(" if counter[char] == 1 else ")"
    return result


assert convert("din") == "((("
assert convert("recede") == "()()()"
assert convert("Success") == ")())())"
assert convert("(( @") == "))(("