# IPV4 Validation without using regex
# split the string by '.'
# check if there are exactly 4 parts
# check if each part is a number between 0 and 255

# without using regex:
def is_valid_ipv4(ips_list):
    valid_ips = []

    for ip in ips_list:
        parts = ip.split('.')

        # must have 4 parts
        if len(parts) != 4:
            continue

        valid = True

        for part in parts:
            # digits check
            if not part.isdigit():
                valid = False
                break

            num = int(part)

            # range check
            if num < 0 or num > 255:
                valid = False
                break

        if valid:
            valid_ips.append(ip)

    return valid_ips

ips_list = ['10.106.228.242','256.100.50.25','10.106.177.179','10.76.30.16']
print(is_valid_ipv4(ips_list))

# with using regex:
import re

def is_valid_ipv4_regex(ips_list):
    valid_ips = []
    pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}' \
              r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'

    # ^ $ to match the whole string (start to end)
    # one ipv4 block
     # 25[0-5] -> 250-255
    # 2[0-4][0-9] -> 200-249
    # 1[0-9]{2} -> 100-199
    # [1-9]?[0-9] -> 0-99 (leading zeroes not allowed)
    # \. -> dot separator
    # ((block)\.){3}) -> three blocks followed by dot
    # (block) -> last block without dot

    for ip in ips_list:
        if re.match(pattern, ip):
            valid_ips.append(ip)
    return valid_ips


ips_list= ['10.106.228.242','256.100.50.25','10.106.177.179','10.76.30.16']
print(is_valid_ipv4_regex(ips_list))





















