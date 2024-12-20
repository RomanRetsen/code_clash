# Author: Cpl Nester
# Script Name: Lab8_2.py
# Description: Script designed to capture that flag
#               by breaking repeating key with ham-length technique


import base64
import socket
import time

KEY_SIZE = 40

# determine hamming length based in values of 2 bytes.
def determine_ham(in_byte1, in_byte2):
    return bin(in_byte1 ^ in_byte2).count("1")


# function determines lowest average value for humming distances
def calculate_keylength_from_encoded_stream(encoded_byte_stream):
    total_length = len(encoded_byte_stream)
    testing_length = (total_length // 40)
    steps_mean_list = []
    for step_length in range(1, KEY_SIZE):
        temp_list = []
        for e in range(0, step_length * testing_length - step_length):
                temp_list.append(determine_ham(encoded_byte_stream[e], encoded_byte_stream[e+step_length]))
        steps_mean_list.append((step_length, sum([x for x in temp_list])/ len(temp_list)))
    # at this moment let's return only one possible length
    # in the future, we can try... let's say top 5
    print(sorted(steps_mean_list, key=lambda x: x[1]))
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
                if (xored_value > 64 and xored_value < 91) \
                        or (xored_value > 96 and xored_value < 123) \
                        or (xored_value) == 32:
                    temp_decoded_letters_count += 1
            the_letter_dict[test_byte] = temp_decoded_letters_count
        possible_key_value = sorted(the_letter_dict.items(), key=lambda x: x[1], reverse=True)
        print(possible_key_value)
        the_key_list.append(possible_key_value[0][0])
    return the_key_list

def attack_xor(stream1, KeySize):
    final_key = []
    LengthStream = len(stream1)
    for position in range(KeySize):
        the_temp_list = [0 for x in range(256)]
        for b in range(256):
            counter = 0
            for i in range(position, LengthStream, KeySize):
                do_xor = b ^ stream1[i]
                if (do_xor > 64 and do_xor < 91) \
                        or (do_xor > 96 and do_xor < 123) \
                        or (do_xor) == 32:
                    counter += 1
            the_temp_list[b] = counter
        # detect index with max_value
        max_value = 0
        max_index = -1
        for index, value in enumerate(the_temp_list):
            if value > max_value:
                max_value = value
                max_index = index
        final_key.append(max_index)
    return final_key

def product_score_for_byte(pos, bt, strm, k_size):
    cntr = 0
    for i in range(pos, len(strm), k_size):
        xor_byte = bt ^ strm[i]
        if (xor_byte >= 65 and xor_byte <= 90) \
                or (xor_byte >= 95 and xor_byte <= 122) \
                or (xor_byte) == 32:
            cntr += 1
    return cntr

def attack_xor2(stream1, k_size):
    cracked_key = []
    for pos in range(k_size):
        the_temp_l = []
        for b in range(256):
            the_temp_l.append((b, product_score_for_byte(pos, b, stream1, k_size)))
        max_value = max(the_temp_l, key=lambda x:x[1])
        cracked_key.append(max_value[0])
    return cracked_key

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
    # detected_key = calc_key_from_encoded_stream_with_knownkeylength(encoded_byte_stream, key_length)
    detected_key = attack_xor2(encoded_byte_stream, key_length)
    return detected_key


# root function for breaking repeating xor encodig data
# that was base64 encoded after encoding
def decrypt_base64_xored_data(encoded_byte_stream_inbase64):
    the_byte_stream = base64.b64decode(encoded_byte_stream_inbase64)
    print(the_byte_stream)
    the_detected_key = calculate_key_from_encoded_stream(the_byte_stream)
    the_encoded_byte_stream = encode_multychar_key(the_byte_stream, the_detected_key)
    return the_encoded_byte_stream


# Function perform connection to server
# and calls decrypt_base64_xored_data
def obtain_data_from_server(host, port):
    print(f"Attempting to connect to server {host} on port {port}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
            stream.connect((host, port))
            print("Connected")
            while True:
                print("data incoming")
                data = stream.recv(5000)
                print(f"Byte stream is {data}")
                data_as_text = data.decode(encoding="ASCII")
                if data_as_text.startswith("Your passphrase"):
                    send_back_data = decrypt_base64_xored_data(data[16:-1])
                    stream.sendall(base64.b64encode(send_back_data))
                    print("Received data de-crypted and sent back")
                elif len(data) > 1 and not data_as_text == "Incorrect" and not data_as_text == "Timeout":
                    print("Flag was received")
                    return base64.b64decode(data).decode("ASCII")
                if not data:
                    break
    except:
        print("Check network settings")
        time.sleep(1)
        exit(2)
    return None


# main function attempting for obrain the flag
# by looping throught dedicated function until successful
def main():
    byte_stream_in_base64 = b"FQBJAC4KDh9MBAcMQSkARRUGClJMPQcCDgB0GABPMgkEVC0NXwxMKgMOQQ8bUkE+BUcWETFICU8sAA0NTBUWQ1ApCUUkAgoTTj0bRzAQMwocADIMAh8fRQZcADEEAEEcBhFFcgAJQg08DUVDKhATFwRFBERFNwlFAE4YF0Q2AAkFWTwJFgAgAAQaTCkaWkU2TAwPTg5SRCAMBg9ZAwkMVDFFAABMERtJADIFCwUBGF4AJQwGEBA6D0VUKgBBEg0GFgxULQ0RQR0HFwA5DAISCnQBCwAjRQsVHkURVQAxBABBCgAdUnI+Dw1ZPRtFSTZFBxseWlNtTClMEQkLTx5PPAwLG1kkDQpQLgBBIwQAAUkAIQNFFQYKCwAzBQtCGjsFAAAkFw4ZU0UyQExlGA0ETgMdTjcFHkIJMQcVTCdFNhwJFxYMRCpMEQkLFlJBPgVHABw4BwtHfUUnFRgNFl4ACA8uBAAVG0VyHhULDT0GAgA2DQRUGwoBSFNlAwNBD08BRSAECAxZIAAEVGILDlQDCxYMVywACUEGChNScicIQhY6DUVDLQgEB0wLFk1SZSAKDgVPE1RyAQ4PWSMHF0srCwZYTAESXk4sAgJBBgYBACEGBAkKdAELADYNBFQCDBREVGUbDQQATwZINxsCRQp0BgpCLQEYVBgNFl5FZTsNABpPFk83GkcKHHQLBFInWkE1AAlTWEggTAkOAAoeWXIZAg0JOA1FdyoAExFMARwMVC0JHEEPAx4AMQYKB1kyGgpNfUUgGABFB0RFZQAKDwsDCwAiDAgSFTFIMkgnFwRUCApTWEggFUUAAgNSQjcFCAwea0gkSG5FDRsDDlNNVGUNCQ1OGxpFcgUIDBw4EUVQJwoRGAlFMkQMZQAKDgVPE1RyCAsOWSAAAAAuCg8RABxTXEUqHAkETioeRTMHCBBZBgECQjtFBR0JAVNFTmUYDQRODBpVIAoPQhg6DEVXIxZBFhkXGklEZQ0JDgAIUlc7HQ9CETEaRU4jCARUIgoRQ0Q8TAYAAwpSZjMdDwcLdCUGaycLGx0JRQRFUCwCAkEaBxcANgAVFlkyGgpNYg0IB0wNEkJENkwEEk4HFwAlCAsJCnQOF08vRRUcCUUUXkEzCUUvAU8dTjdJEAMKdBsEVicBQTUACVNYSCBMCQ4ACh5ZchkCDQk4DUUIAw1NVAAKHEcAJBhFAAIDUlQ6DEcOFjoNCVliFQQbHAkWBQASBAATC08WT3IdDwcAdAkJTGIGDhkJRRVeTyhTRSACA1JUOgxHDhY6DQlZYhUEGxwJFgwIBARJQQIAHUtyCBNCGDgERVQqAEEYAwsWQFllHAAOHgMXCXI+DwcLMUgBT2IRCREVRRJATGUOAA0BARUf"
    print(decrypt_base64_xored_data(byte_stream_in_base64))
#     host = '10.50.10.2'
#     port = 1234
#     while True:
#         the_flag = obtain_data_from_server(host, port)
#         if not the_flag is None:
#             print(f"The flag is: {the_flag}")
#             break
#         else:
#             print("Failed to decode flag in this round!!! \n Let me try again!")
#             time.sleep(2)


if __name__ == '__main__':
    main()
