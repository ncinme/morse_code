import pandas

# Reading csv file containing morse code chart/table
data = pandas.read_csv("morse_code.csv")
morse_code_dict = dict(zip(data['character'].to_list(), data['code'].to_list()))

# Prompting user for input text
input_text = ""
while not input_text:
    input_text = input("Please enter the text you want to convert to morse code: ")

# Converting input text to morse code
morse_code = ""

try:
    for char in input_text.upper():
        if char == " ":
            morse_code += char
        else:
            morse_code += morse_code_dict[char]

except KeyError as err:
    print(f"Error!! Invalid key: {err}")

except:
    print("Error!! Try again.")
else:
    print(f"Your text '{input_text}'")
    print(f"Corresponding Morse code: {morse_code}")
