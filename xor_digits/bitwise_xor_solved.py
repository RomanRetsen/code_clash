from datetime import datetime, timedelta, time

binary_view = {0:'1111110', 1:'0110000', 2:'1101101', 3:'1111001', 4:'0110011',
               5:'1011011', 6: '1011111', 7: '1110000', 8: '1111111', 9: '1111011'}

def process_time(time_input):
    total = 0
    hr, min = time_input.split(':')
    input_date = datetime(2020, 1,1, int(hr), int(min),0,0)
    delta_date = input_date + timedelta(minutes=1)

    input_hr_tens = binary_view[int(str(input_date.hour).rjust(2, "0")[0])]
    input_hr_singles = binary_view[int(str(input_date.hour).rjust(2, "0")[1])]
    input_min_tens = binary_view[int(str(input_date.minute).rjust(2, "0")[0])]
    input_min_singles = binary_view[int(str(input_date.minute).rjust(2, "0")[1])]

    delta_hr_tens = binary_view[int(str(delta_date.hour).rjust(2, "0")[0])]
    delta_hr_singles = binary_view[int(str(delta_date.hour).rjust(2, "0")[1])]
    delta_min_tens = binary_view[int(str(delta_date.minute).rjust(2, "0")[0])]
    delta_min_singles = binary_view[int(str(delta_date.minute).rjust(2, "0")[1])]

    print(delta_hr_tens)
    print(len(delta_hr_tens))
    for i in range(7):
        print(str(delta_hr_tens[i]))
        total += (int(delta_hr_tens[i]) ^ int(input_hr_tens[i])) \
                + (int(delta_hr_singles[i]) ^ int(input_hr_singles[i])) \
                + (int(delta_min_tens[i]) ^ int(input_min_tens[i])) \
                + (int(delta_min_singles[i]) ^ int(input_min_singles[i]))

    return total


if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        input_time = input()
        print(process_time(input_time))
