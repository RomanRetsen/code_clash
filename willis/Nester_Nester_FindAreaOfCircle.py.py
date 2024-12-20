import Nester_FindAreaOfCircle


if __name__ == "__main__":
    while True:
        if (converted_radius := Nester_FindAreaOfCircle.is_valid_radius( \
                input("Enter circle's radius >> "))) == -1:
            print("You've entered invalid radius value. Try again!")
        else:
            print(f"Rounded to two digits after the comma, circle's area is " \
                  f"{Nester_FindAreaOfCircle.calculate_circle_area(converted_radius)}")
            break