import re

def validate_aadhaar(aadhaar):
    pattern = r'^\d{12}$'
    return bool(re.match(pattern, aadhaar))


print(validate_aadhaar("123456789012"))  # True




def is_lowercase(text):
    pattern = r'^[a-z]+$'
    return bool(re.match(pattern, text))

print(is_lowercase("hello"))   # True
print(is_lowercase("Hello"))   # False




def validate_roll(roll):
    pattern = r'^[A-Z]{2}\d{4}-\d{3}$'
    return bool(re.match(pattern, roll))

# Example
print(validate_roll("CS2024-101"))  # True




def valid_password(password):
    pattern = r'^[A-Za-z0-9]+$'
    return bool(re.match(pattern, password))

# Example
print(valid_password("Pass123"))   # True
print(valid_password("Pass@123"))  # False




def valid_password(password):
    pattern = r'^[A-Za-z0-9]+$'
    return bool(re.match(pattern, password))

# Example
print(valid_password("Pass123"))   # True
print(valid_password("Pass@123"))  # False



def count_vowels(text):
    pattern = r'[aeiouAEIOU]'
    vowels = re.findall(pattern, text)
    return len(vowels)

# Example
print(count_vowels("Hello World"))  # 3