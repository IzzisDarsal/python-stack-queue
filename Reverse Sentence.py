#Percobaan 3
def reverse_sentence(sentence):
    stack = []
    reversed_sentence = ""

    for word in sentence.split():
        stack.append(word)

    while len(stack)>0:
        reversed_sentence += stack.pop()+""

    return reversed_sentence.strip()
sentence = "Selamat Pagi, bagaimana kabar Anda?"
print(reverse_sentence(sentence))