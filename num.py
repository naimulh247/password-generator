import itertools

our_list = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", 
"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
 "1","2","3","4","5","6","7","8","9",'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/')

for L in range(0, len(our_list)+1):

    for subset in itertools.combinations(our_list, L):

        passw = ''.join(subset)
        f = open("password.txt", "a")
        f.write(passw+'\n')

        # print(''.join(subset))
        print(*subset, sep='')
        # f = open("password.txt", "a")
        # f.write("".join(subset))