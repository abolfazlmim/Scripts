import os

# print all environment variables as a dictionary
print(os.environ)

# get LANG HOME variable without KeyError
print(os.environ.get("LANG"))
print(os.environ.get("HOME"))
#Create custom variable and Pritn it !
os.environ["MY_CUSTOM_KEY"] = "secret_value"
print(os.environ.get("MY_CUSTOM_KEY"))
