
import hashlib,binascii

hashInput = input("INPUT NTLM Hash : ")

print("Import file...")
text_file = "hk_hlm_founds.txt"


my_file = open(text_file, "r", encoding='utf8')

print("Reading...")
word_list = my_file.read().splitlines()

print("Sorting...")
word_list = sorted(word_list)

def hashNTLM(word):
    hash = hashlib.new('md4', word.encode('utf-16le')).digest()
    return binascii.hexlify(hash)


def main():
    for world_i in word_list:
        print(world_i)
        hashWord = hashNTLM(world_i).decode("utf-8")
        print(hashWord)
        print()
        if (hashInput == hashWord):
            print("SUCCESS!! WORD IS : ", world_i)
            break

main()
