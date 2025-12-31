sen = ["Python is good", "Python is good python module", "hello world", "This is good"]
user = input("Enter query: ")

def searching_tool(keyword, lst):
    keyword = keyword.lower()
    user_lst = keyword.split(" ")

    for i in range(len(lst)):
        lst[i] = lst[i].lower()

    sentence_dict = {}
    for sentence in lst:
        sentence_dict[sentence] = 0
        for user_word in user_lst:
            if user_word in sentence :
                sentence_dict[sentence] += sentence.count(user_word)

    new_sentence_dict = dict(sorted(sentence_dict.items(), key=lambda item: item[1], reverse=True))

    final_lst = []
    for key, value in new_sentence_dict.items():
        if value > 0:
            final_lst.append(key)
    return final_lst

print(searching_tool(user, sen))