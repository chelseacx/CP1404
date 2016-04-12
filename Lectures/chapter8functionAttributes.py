
# docstring

def subject(subject_code, subject_name):
    """
    This is a function for printing subject name and code
    """
    string_result = "This subject {} refers to {}".format(subject_code, subject_name)
    print(string_result)
    return string_result

print(subject.__doc__) #doc attributes of function

# annotation
def subject2(subject_code: str, subject_name: str)-> int:
    string_result = "This subject {} refers to {}".format(subject_code, subject_name)
    print(string_result)
    return string_result

print(subject2.__annotations__)
print(subject2.__name__)