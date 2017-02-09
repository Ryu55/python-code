#a program that can convert your age into seconds or years

def age_converter():
    print("Hello! This is an age converter. We can convert your age from years into months, weeks, days, hours, minutes, and seconds!")

    user_age = input("Enter your age in years (i.e. - 25): ")
    user_age = int(user_age)

    months = user_age * 12
    weeks = user_age * 52
    days = user_age * 365
    hours = user_age * 24 * 365
    minutes = user_age * 60 * 24 * 365
    seconds = user_age * 60 * 60 * 24 * 365

    print("Your age in months is {}".format(months))
    print("Your age in weeks is {}".format(weeks))
    print("Your age in days is {}".format(days))
    print("Your age in hours is {}".format(hours))
    print("Your age in minutes is {}".format(minutes))
    print("Your age in seconds is {}".format(seconds))


age_converter()
