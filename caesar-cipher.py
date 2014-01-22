# Caesar cipher program
# Annamalai Nagappan Wed 22,2014 11.40PM

print " Caesar cipher encryption"
message=raw_input("Enter the message to be encrypted ")
mode=raw_input("type encrypt or decrypt ")
key=input("Enter the key ")
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translated=''
message=message.upper()

for symbols in message:
	if symbols in LETTERS:
		num=LETTERS.find(symbols)
		if mode=="encrypt":
			num+=key
		elif mode=="decrypt":
			num-=key
		if num>len(LETTERS):
			num-=len(LETTERS)
		elif num<0:
			num+=len(LETTERS)
		translated=translated+LETTERS[num]
	else:
		translated=translated+symbols
print translated
