a_string = "this string\nis a \t\tmusical thread"
print(a_string)
"""
    ASCII characters can be used instead of \n or \t
"""
b_string = "this string" + chr(10) + "is a" + chr(9) + chr(9) + "musical thread"
print(b_string)

raw_string = r"this striing\nis a \t\tmusical thread"
print(raw_string)

backslash_string = "this string is \followed by backslash"
print(backslash_string)
backslash_string2 = "this string is \\followed by backslash"
print(backslash_string2)
"""
Unwanted error
"""
# error_string = "this string have error \"
"""
so instead do this"""
no_error_string = "this string have no error \\"
print(no_error_string)
