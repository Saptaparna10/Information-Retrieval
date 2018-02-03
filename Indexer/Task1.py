from bs4 import BeautifulSoup
import os
import operator
import glob
import re
import traceback
import string

# Getting the path of the current directory 
PRESENT_DIR = os.getcwd()
# LIST_OF_FILES maintains names of files
LIST_OF_FILES = []

# get wikipedia articles downloaded in HW1
def get_content():
    try:
        path = os.path.join(PRESENT_DIR, 'articles_hw1')
        for filename in glob.glob(os.path.join(path,'*.txt')):
            with file(filename) as f:
                url = f.readline()
                file_name = (url.split("https://en.wikipedia.org/wiki/"))[1][:-1]
                print 'Generating corpus for ' + file_name
                content = f.read()
                content = content.lower()
                if (content.find('<span class="mw-headline" id="see_also">')!=-1):
                    content=content[:content.index('<span class="mw-headline" id="see_also">')]
                elif (content.find('<span class="mw-headline" id="references">')!=-1):
                    content=content[:content.index('<span class="mw-headline" id="references">')]
                elif (content.find('<span class="mwe-math-element">')!=-1):
                    content=content[:content.index('<span class="mwe-math-element">')]
                elif (content.find('<table class="wikitable">')!=-1):
                    content=content[:content.index('<table class="wikitable">')]
                if (content.find('<div class="toc" id="toc">')!=-1):
                    first=content[:content.index('<div class="toc" id="toc">')]
                    second=content[content.find('</div>', (content.find('</div>',(content.index('<div class="toc" id="toc">') + 1)) + 1)):]
                    content = first+second

                soup = BeautifulSoup(content, "html.parser")
                soup.prettify().encode("utf-8")
                title = soup.find('title').get_text().encode("utf-8")
                header = soup.find('h1').get_text().encode("utf-8")
                raw_data = soup.findAll('div', attrs={'id':'bodycontent'})
                body= ""
                for div in raw_data:
                    body=div.get_text().encode("utf-8")
                content = title + header + body
                tokenized_text = tokenize(content)
                write_to_file(tokenized_text,file_name)
    except:
        print "Error in try block of get_content!"
        print traceback.format_exc()

# Tokenize raw data
def tokenize(content):
    content = re.sub(r'[@_!\s^&*?#=+$~%:;\\/|<>(){}[\]"\']' , ' ', content)
    tokenized_words = []
    for word in content.split():
        tokenized_words.append(word.strip(string.punctuation))
        word_length = len(word)
        if word[word_length - 1:word_length] == "-" or word[word_length - 1:word_length] == "," or word[word_length - 1:word_length] == ".":
            word = word[:(len(word)-1)]
            tokenized_words.append(delete_preceeding_punctuation(word))
        else:
            tokenized_words.append(delete_preceeding_punctuation(word))
    tokenized_words = [x for x in tokenized_words if x != '']
    tokenized_words = " ".join(tokenized_words)    
    return tokenized_words

# Handle punctuations
def delete_preceeding_punctuation(word):

    while(word[:1] == "-" or word[:1] == "," or word[:1] == "."):
        # Handle numbers
        if re.match(r'^[\-]?[0-9]*\.?[0-9]+$', word):
            return word
        if word[:1] == "-" or word[:1] == "." or word[:1] == ",":
            word = word[1:]
        else:
            return word
    return word

# Write tokenized words to file
def write_to_file(tokenized_text,file_name):
    try:
        index_value=1
        if file_name not in LIST_OF_FILES:
            LIST_OF_FILES.insert(0,file_name)
        else:
            while(file_name in LIST_OF_FILES):
                file_name = file_name+str(index_value)
                index_value = index_value + 1
            LIST_OF_FILES.insert(0,file_name)
        if not os.path.exists(PRESENT_DIR+"\\"+"corpus"):
             os.makedirs(PRESENT_DIR+"\\"+"corpus")
        file_index_terms= open(PRESENT_DIR+"\\"+"corpus"+"\\"+file_name+".txt",'w')
        file_index_terms.write(tokenized_text)
        file_index_terms.close()
    except:
        print "Error in try block of write_content!"
        print traceback.format_exc()
        
# main function
def main():

    print "Generating the corpus..."
    get_content()


if __name__ == "__main__": main()