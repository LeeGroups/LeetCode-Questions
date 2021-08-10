import collections
import math

def reorganizeString(s):
    letters = collections.defaultdict(int)
    most_occ = 0
    length = len(s)
    for i in range(length):
        letters[s[i]] += 1
        most_occ = max(letters[s[i]], most_occ)
    half = math.ceil(length / 2)
    if most_occ > half:
        return ""
    output = ""
    list_of_letters = []
    for elem in letters:
        list_of_letters.append([letters[elem],elem])
    list_of_letters.sort(reverse=True)
    
    even = 0
    odd = 1
    sum = list_of_letters[0][0]
    while sum < half:
        sum += list_of_letters[odd][0]
        odd += 1    
    while sum > 0:
        if sum > half:
            odd -= 1
            diff = sum-half
            a = list_of_letters[even][1] + list_of_letters[odd][1]
            output += a * diff
            list_of_letters[even][0] -= diff
            list_of_letters[odd][0] -= diff
            sum = half
            odd += 1
        else:
            if even == len(list_of_letters):
                break
            elif list_of_letters[even][0] > 0:
                output += list_of_letters[even][1]
                list_of_letters[even][0] -= 1
            else:
                even += 1 
                continue
            if list_of_letters[odd][0] > 0:
                output += list_of_letters[odd][1]
                list_of_letters[odd][0] -= 1
                sum -= 1
            else: 
                if odd + 1 == len(list_of_letters):
                    break
                else:
                    odd += 1
                    output += list_of_letters[odd][1]
                    list_of_letters[odd][0] -= 1
                    sum -= 1
    return output
    
# Sample inputs

# Expect "aba"
print(reorganizeString("aab"))

# Expect ""
print(reorganizeString("aaa"))

# Expect "cacacab"
print(reorganizeString("aaabbbccc"))

# Expect "gvgqepemy"
print(reorganizeString("eqmeyggvp"))

# Expect "gvgqepemy"
print(reorganizeString("ogccckcwmbmxtsbmozli"))