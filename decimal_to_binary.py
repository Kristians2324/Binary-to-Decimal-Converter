# Function to convert decimal to binray with Max
def dec_to_bin(dec_num):
    if dec_num == 0:
        return "0"
    bin_num = ""
    while dec_num > 0:
        bin_num = str(dec_num % 2) + bin_num
        dec_num = dec_num // 2
print(bin_num) 



