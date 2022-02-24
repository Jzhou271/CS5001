'''
This is file contains a function to take a day name in English,
and return the name in French,
It also contains tests, to ensure that we are correctly implementing
this function
'''


def translate(day_name):
    '''
    Takes a day name in English and returns the corresponding name in French
    :param day_name: a string representing the name of a day of the week
    in English
    :return: a string representing the name of day_name but in French
    '''
    french_day = ""
    if day_name == "Monday":
        french_day = "lundi"
    elif day_name == "Tuesday":
        french_day = "mardi"
    elif day_name == "Wednesday":
        french_day = "mercredi"
    elif day_name == "Thursday":
        french_day = "jeudi"
    elif day_name == "Friday":
        french_day = "vendredi"
    elif day_name == "Saturday":
        french_day = "samedi"
    elif day_name == "Sunday":
        french_day = "dimanche"
    return french_day


def test_translate(english_day, expected):
    actual = translate(english_day)
    if actual != expected:
        print('TEST FAILED')
        print(english_day)
        print('EXPECTED:', expected)
        print('ACTUAL:', actual)
    else:
        print("TEST PASSED")
        print(english_day)
        print('EXPECTED:', expected)
        print('ACTUAL:', actual)


def main():
    test_translate("Monday", "lundi")
    test_translate("Tuesday", "mardi")
    test_translate("Wednesday", "mercredi")
    test_translate("Thursday", "jeudi")
    test_translate("Friday", "vendredi")
    test_translate("Saturday", "samedi")
    test_translate("Sunday", "dimanche")


if __name__ == "__main__":
    main()
