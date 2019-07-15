import re

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    query=phoneNumRegex.search("Is there a number here" + text)
    print("Phone number found:" + query.group())

isPhoneNumber("443-323-3434")