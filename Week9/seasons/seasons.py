from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birth_date = input("Date of birth: ")
    try:
        birth_date = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid Date")
    minutes_age = convert_time(birth_date)
    output = add_text(minutes_age)
    print(output)

def convert_time(birth_date):
    date_today = date.today()
    delta = date_today - birth_date
    minutes_age = delta.days * 24 * 60
    return minutes_age

def add_text(minutes_age):
    text = p.number_to_words(minutes_age).replace(" and", "")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()
