import pandas

alp_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

alphebetic_dic = {row.letter:row.code for (index, row) in alp_dataframe.iterrows()}
print(alphebetic_dic)
while True:
    name = input("Enter a word:").upper()
    try:
        phonetic_code = [alphebetic_dic[i] for i in name]
    except:
        print("Sorry, only letters in the alphabet please.")
    else:
        phonetic_code = [alphebetic_dic[i] for i in name]
        break
print(phonetic_code)