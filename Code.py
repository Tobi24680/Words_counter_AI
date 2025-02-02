import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')

para = input('Enter A Paragraph:\n')
list_1 = word_tokenize(para)
list_2 = [i for i in list_1 if i not in {',', '.', ';', ':', '!', '?'}]
print("the total no of paragraph is :", len(list_2))

set_1 = set()
for i in list_2:
    if i not in set_1:
        list_3 = list_2.count(i)
        print(f" '{i}' No of occurences is = {list_3}")
        set_1.add(i)
      
