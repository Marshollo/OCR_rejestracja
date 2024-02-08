import pytesseract
from PIL import Image
import re
import csv

image = Image.open('rej1.png')
text = pytesseract.image_to_string(image)
print(text)
text_nospace = text.replace(" ", "")


def validation(tekst):
    # checks that the registration number is correct, i.e. it has 2 or 3 letters and then followed by either 5 digits
    # or 4 digits plus one letter.
    pattern = r'^[A-Za-z]{2,3}(\d{4}[A-Za-z]|\d{5})$'

    if re.match(pattern, tekst):
        litera = text_nospace[0].upper()
        with open('wojewo.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if litera == row['Litera']:
                    print("Prawidłowy format tablicy rejestracyjnej")
                    print(row['Wojewodztwo'])
    else:
        print("Błędny format rejestracji")


validation(text_nospace)
