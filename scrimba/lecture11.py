msg='welcome to Python 101: Strings'
new_msg = msg[18] + msg[7] + msg[0:7] + msg[7] + msg[25:29] + msg[7:10] + msg[7] + msg[13] + msg[12] + msg[2] + msg[1] + msg[25]
reversed_new_msg = new_msg[::-1]
print(msg)
print(new_msg.title())
print(reversed_new_msg)