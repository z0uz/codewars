def rev_rot(s, sz):
    if sz <= 0 or len(s) == 0 or sz > len(s):
        return ""
    
    def rotate(strg):
        return strg[1:] + strg[0]

    def reverse(strg):
        return strg[::-1]

    def cube_sum(strg):
        return sum(int(digit)**3 for digit in strg)

    chunks = [s[i:i+sz] for i in range(0, len(s), sz)]

    modified_chunks = []
    for chunk in chunks:
        if len(chunk) == sz:
            if cube_sum(chunk) % 2 == 0:
                modified_chunks.append(reverse(chunk))
            else:
                modified_chunks.append(rotate(chunk))

    return ''.join(modified_chunks)

def testing(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"
