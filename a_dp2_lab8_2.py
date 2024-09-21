# Author: Cpl Nester
# Script Name: Lab8_2.py
# Description: Script designed to capture that flag
#               by breaking repeating key with ham-length technique


import base64
import socket
import time


# determine hamming length based in values of 2 bytes.
def determine_ham(in_byte1, in_byte2):
    return bin(in_byte1 ^ in_byte2).count("1")


# function determines lowest average value for humming distances
def calculate_keylength_from_encoded_stream(encoded_byte_stream):
    total_length = len(encoded_byte_stream)
    # testing_length = (total_length // 40) * 40
    testing_length = (total_length // 40) * 40
    steps_mean_list = []
    for step_length in range(1, testing_length//40):
        temp_list = []
        for e in range(0, (testing_length-step_length), step_length):
            temp_list.append(determine_ham(encoded_byte_stream[e], encoded_byte_stream[e+step_length]))
        steps_mean_list.append((step_length, sum([x for x in temp_list])/ len(temp_list)))
    # at this moment let's return only one possible length
    # in the future, we can try... let's say top 5
    return sorted(steps_mean_list, key=lambda x: x[1])[0][0]


# Core function that  brute force all possible key value for each position in the key
# and determines/counts number of decoded values being legit characters and spaces
def calc_key_from_encoded_stream_with_knownkeylength(encoded_byte_stream, key_length):
    the_key_list = []
    encoded_byte_stream_length = len(encoded_byte_stream)
    for key_position in range(key_length):
        the_letter_dict = {x:0 for x in range(255)}
        for test_byte in range(255):
            temp_decoded_letters_count = 0
            for char_index in range(key_position, (encoded_byte_stream_length - key_length), key_length):
                xored_value = test_byte ^ encoded_byte_stream[char_index]
                if (xored_value > 64 and xored_value < 91) or (xored_value > 96 and xored_value < 123) or (xored_value) == 32:
                    temp_decoded_letters_count += 1
            the_letter_dict[test_byte] = temp_decoded_letters_count
        possible_key_value = sorted(the_letter_dict.items(), key=lambda x: x[1], reverse=True)
        the_key_list.append(possible_key_value[0][0])
    return the_key_list


# using modulas function for cycle the key
def encode_multychar_key(input_str, key):
    key_len = len(key)
    the_result = []
    for index, the_byte in enumerate(input_str):
        the_result.append(the_byte ^ key[index % key_len])
    return b"".join([x.to_bytes(1, "big") for x in the_result])


# function for decrypting the xor-key
def calculate_key_from_encoded_stream(encoded_byte_stream):
    key_length = calculate_keylength_from_encoded_stream(encoded_byte_stream)
    detected_key = calc_key_from_encoded_stream_with_knownkeylength(encoded_byte_stream, key_length)
    return detected_key


# root function for breaking repeating xor encodig data
# that was base64 encoded after encoding
def decrypt_base64_xored_data(encoded_byte_stream_inbase64):
    the_byte_stream = base64.b64decode(encoded_byte_stream_inbase64)
    the_detected_key = calculate_key_from_encoded_stream(the_byte_stream)
    the_encoded_byte_stream = encode_multychar_key(the_byte_stream, the_detected_key)
    return the_encoded_byte_stream


# Function perform connection to server
# and calls decrypt_base64_xored_data
def obtain_data_from_server(host, port):
    print(f"Attempting to connect to server {host} on port {port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
            stream.connect((host, port))
            print("Connected")
            while True:
                print("data incoming")
                data = stream.recv(5000)
                data_as_text = data.decode(encoding="ASCII")
                if data_as_text.startswith("Your passphrase"):
                    send_back_data = decrypt_base64_xored_data(data[16:-1])
                    stream.sendall(base64.b64encode(send_back_data))
                    print("Received data de-crypted and sent back")
                elif len(data) > 1 and not data_as_text == "Incorrect" and not data_as_text == "Timeout":
                    print("Flag was received")
                    return data_as_text
                if not data:
                    break
    except:
        print("Check network settings")
        time.sleep(1)
        exit(2)
    return None


# main function attempting for obtain the flag
# by looping throught dedicated function until successful
def main():
    host = '10.50.10.2'
    port = 1234
    while True:
        the_flag = obtain_data_from_server(host, port)
        if not the_flag is None:
            print(f"The flag is: {the_flag}")
            break
        else:
            print("Failed to decode flag in this round!!! \n Let me try again!")
            time.sleep(2)


if __name__ == '__main__':
    main()
