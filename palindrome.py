def palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


def palindrome2(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome2("bearaeb")); # true
print(palindrome2("Whatever revetahW")); # true
print(palindrome2("Aloha, how are you today?")); # false
