# Function to implement the KMP algorithm
def check(text, pattern):

    # base case 1: pattern is empty
    if not pattern:
        print('The pattern occurs with shift 0')
        return

    # base case 2: text is empty, or text's length is less than that of pattern's
    if not text or len(pattern) > len(text):
        print('Pattern not found')
        return

    chars = list(pattern)

    # next[i] stores the index of the next best partial match
    next = [0] * (len(pattern) + 1)
    for i in range(1, len(pattern)):
        j = next[i + 1]

        while j > 0 and chars[j] is not chars[i]:
            j = next[j]

        if j > 0 or chars[j] == chars[i]:
            next[i + 1] = j + 1

    j = 0
    for i in range(len(text)):
        if j < len(pattern) and text[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                l = i-j+1
                u = ""
                for i in range(0, len(pattern)):
                    u = u+"*"
                c = text.replace(text[l:l+len(pattern)], u)
                return c
                #print('Pattern occurs with shift', (i - j + 1))
        elif j > 0:
            j = next[j]
            i = i - 1        # since `i` will be incremented in the next iteration
    return text

# Program to implement the KMP algorithm in Python

def KMP(content):
    text = content.lower()
    pattern = ["fuck", "bitch", "asshole"]
    for x in pattern:
        text = check(text, x)
    print("returnin"+text)
    return text




