# Given a non-empty string like "Code" return a string like "CCoCodCode".

# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"

def stringSplosion(str):
    result = []
    for i in range(len(str)):
        result.append(str[0:i+1])

    return ''.join(result)


str = "Code"

print(stringSplosion(str))