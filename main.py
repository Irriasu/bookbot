def open_file(file_path):
    with open (file_path) as f:
        file_contents = f.read()
        return file_contents

def count_word(text):
    words = text.split()
    return len(words)

def char_count(text):
    dict = {}
    chars = text.lower()
    for char in chars:
        if char in dict:
            dict[char]+=1
        else :
            dict[char]=1
    return dict   

def sort_on(dict):
    return dict["char"]


def sort_dict(dict):
    dict_list = [{'char':key,'count':value} for key,value in dict.items() ]
    dict_list.sort(reverse=False,key=sort_on)
    return dict_list

def filter_alpha(list):
    new_list =[]
    for i in list:
        if i["char"].isalpha():
            new_list.append(i)
    return new_list


def main():
    content = open_file("books/frankenstein.txt")
    content_count = count_word(content)
    chars = char_count(content)
    chars = sort_dict(chars)
    chars = filter_alpha(chars)
    my_report = report(content_count,chars)
    print (my_report)

def report(count,list):
    report = f"--- Begin report of books/frankenstein.txt --- \n {count} words found in the document \n\n"
    for i in list:
        report+= f'The {i["char"]} character was found {i["count"]} times \n'
    return report

main()
