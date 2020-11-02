def ceasar(text: str, key: int) -> str:
    result = ""  # type: str
    for char in text:
        c: int = ord(char)
        enc_char: str = chr(c + key)
        result += enc_char
    return result


print(ceasar("subscribe", 2))
print(ceasar("uwduetkdg", -2))