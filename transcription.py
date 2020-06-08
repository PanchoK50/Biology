sequence = input("Enter organic base sequence: \n").upper()

c = "C"
g = "G"
a = "A"
t = "T"
u = "U"

transcription = []



def ask_mode():
    mode = input("RNA-transcription [R] or DNA-transcription [D]: \n")
    if mode.upper() == "R":
        ut = "U"
    if mode.upper() == "D":
        ut = "T"
    if mode.upper() != "R" and mode.upper() != "D": ask_mode()
    return ut

ut = ask_mode()

for i in sequence:
    if i == c:
        transcription.append(g)
    if i == g:
        transcription.append(c)
    if i == t:
        transcription.append(a)
    if i == u:
        transcription.append(a)
    if i == a:
        transcription.append(ut)

new_sequence = "".join(transcription)
print(new_sequence)



