text = "This is the simple brute force approach for n-gram"
text_list = text.split()
ngram = []
for i in range(0,len(text_list)):
    if i+1 < int(len(text_list)):
        add = (text_list[i],text_list[i+1])
        if add:
            ngram.append(add)
    else:
        print("Ngramming done, printing Ngram . . . ")

print(ngram)