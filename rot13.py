def rot13(message):
    def shift_char(char, shift):
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + shift) % 26 + base)

    result = ""
    for char in message:
        if char.isalpha():
            result += shift_char(char, 13)
        else:
            result += char
    return result

# Test the function
message = "Hello, World!"
ciphered_text = rot13(message)
print(ciphered_text)
