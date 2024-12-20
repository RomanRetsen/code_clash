import math


#function sanitize user inputted radius value
def is_valid_radius(radius_as_string):
    try:
        float_r = float(radius_as_string)
        return float_r if float_r >= 0 else -1
    except ValueError:
        return -1

#calculated circle's area based on radius
def calculate_circle_area(r_as_float):
    return round((r_as_float ** 2) * math.pi, 2)


if __name__ == "__main__":
    while True:
        if (converted_radius := is_valid_radius(input("Enter circle's radius >> "))) == -1:
            print("You've entered invalid radius value. Try again!")
        else:
            print(f"Rounded to two digits after the comma, circle's area is " \
                  f"{calculate_circle_area(converted_radius)}")
            break