import io
import glob
import operator
import os
import traceback
from pprint import pprint

# Inverted index for unigram
def inverted_index_for_unigram():
    # term -> (docid,tf)
    inverted_index = {}
    # docid -> tf
    doc_id_tf_dict = {}
    number_of_Token = {}
    try:
        directory_name = os.getcwd()
        path = os.path.join(directory_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                document =f.read()
                file_name = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_name
                number_of_Token[file_name] = len(document.split())
                for word in document.split():
                    if not inverted_index.has_key(word):
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word] =  doc_id_tf_dict
                    elif inverted_index[word].has_key(file_name):
                        doc_id_tf_dict = inverted_index[word]
                        value = doc_id_tf_dict[file_name]
                        value = value + 1
                        doc_id_tf_dict[file_name] = value
                    else:
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word].update(doc_id_tf_dict)
            f.close()
        print "toeken count : " 
        print number_of_Token
    except:
        print "Error in try block of inverted_index_for_unigram!"
        print traceback.format_exc()
    return inverted_index

def make_term_freq_table(inverted_index,ngram):

    term_frequency = {}
    for term in inverted_index:
        frequency = 0
        doc_id_tf_dict = inverted_index[term]
        for doc_id in doc_id_tf_dict:
            frequency = frequency + doc_id_tf_dict[doc_id]
        term_frequency[term] = frequency
    sorted_term_frequency = sorted(term_frequency.items(), key=operator.itemgetter(1), reverse=True)
    write_term_frequency_to_file(sorted_term_frequency,ngram)
    return sorted_term_frequency


def write_term_frequency_to_file(term_frequency,ngram):

    try:
        print "Writing term frequency table..."
        file_name= "term_frequency" + "_" + str(ngram) + ".txt"
        file_term_frequency= open(file_name, 'w')
        table_form = '{:<30}' * 2
		
        for term in term_frequency:
            file_term_frequency.write(table_form.format(str(term[0]),str(term[1])))        
            file_term_frequency.write("\n")
        file_term_frequency.close()
    except:
        print "Error in try block of write_term_frequency_to_file!"
        print traceback.format_exc()

def make_doc_freq_table(inverted_index,ngram):
    document_freq = {}

    for term in inverted_index:
        document_list = []
        doc_dict = inverted_index[term]
        for doc_id in doc_dict:
            document_list.append(doc_id)
        document_freq[term] = document_list

    sorted_document_freq = sorted(document_freq.items(), key=operator.itemgetter(0))
    write_document_freq(sorted_document_freq, ngram)
    return sorted_document_freq

# generates file with doc frequency table
def write_document_freq(document_freq, ngram):

    try:
        print "Writing document frequency table..."
        file_name= "doc_freq_table" + "_" + str(ngram) + ".txt"
        file_doc_freq_table= open(file_name, 'w')
        for list in document_freq:
            table_form_doc = '{:<10}' * 3
            list_length = len (list[1])
            file_doc_freq_table.write(table_form_doc.format((str(list[0])),(str(list[1])),(str(list_length))))
            file_doc_freq_table.write("\n")
        file_doc_freq_table.close()
    except:
        print "Error in try block of write_doc_freq!"
        print traceback.format_exc()



def inverted_index_for_bigram():

    # term -> (docid,tf)
    inverted_index = {}
    # docid -> tf
    doc_id_tf_dict = {}
    number_of_Token = {}
    try:
        directory_name = os.getcwd()
        path = os.path.join(directory_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                document =f.read()
                file_name = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_name
                words = document.split()
                number_of_Token[file_name] = len(words)-1
                for i in range(len(words) - 1) :
                    word = words[i] + " " + words[i+1]
                    if not inverted_index.has_key(word):
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word] =  doc_id_tf_dict
                    elif inverted_index[word].has_key(file_name):
                        doc_id_tf_dict = inverted_index[word]
                        value = doc_id_tf_dict[file_name]
                        value = value + 1
                        doc_id_tf_dict[file_name] = value
                    else:
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word].update(doc_id_tf_dict)
            f.close()
        print "toeken count : " 
        print number_of_Token


    except:
        print "Error in try block of inverted_index_for_unigram!"
        print traceback.format_exc()
    return inverted_index

def inverted_index_for_trigram():

    # term -> (docid,tf)
    inverted_index = {}
    # docid -> tf
    doc_id_tf_dict = {}
    number_of_Token = {}
    try:
        directory_name = os.getcwd()
        path = os.path.join(directory_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                document =f.read()
                file_name = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_name
                words = document.split()
                number_of_Token[file_name] = len(words)-2
                for i in range(len(words) - 2) :
                    word = words[i] + " " + words[i+1] + " " + words[i+2]
                    if not inverted_index.has_key(word):
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word] =  doc_id_tf_dict
                    elif inverted_index[word].has_key(file_name):
                        doc_id_tf_dict = inverted_index[word]
                        value = doc_id_tf_dict[file_name]
                        value = value + 1
                        doc_id_tf_dict[file_name] = value
                    else:
                        doc_id_tf_dict = {file_name : 1}
                        inverted_index[word].update(doc_id_tf_dict)
            f.close()
        print "toeken count : " 
        print number_of_Token


    except:
        print "Error in try block of inverted_index_for_unigram!"
        print traceback.format_exc()
    return inverted_index

# generates file with doc frequency table
def write_inverted_index(inverted_index, ngram):

    try:
        print "Writing inverted index..."
        file_name= "inverted_index" + "_" + str(ngram) + ".txt"

        with open(file_name, 'wt') as out:
            pprint(inverted_index, stream=out)
          
    except:
        print "Error in try block of write_doc_freq!"
        print traceback.format_exc()

# main function
def main():
    n = raw_input ('Please enter value of n for n-grams...')

    if int(n)==1:
        # Unigram
        index_for_unigrams = inverted_index_for_unigram()
        write_inverted_index(index_for_unigrams,"unigram")
        term_freq_table_for_unigram = make_term_freq_table(index_for_unigrams, "unigram")
        doc_freq_table_for_unigram = make_doc_freq_table(index_for_unigrams, "unigram")

    elif int(n)==2:
        # Bigram
        index_for_bigrams = inverted_index_for_bigram()
        write_inverted_index(index_for_bigrams,"bigram")
        term_freq_table_for_bigram = make_term_freq_table(index_for_bigrams, "bigram")
        doc_freq_table_for_bigram = make_doc_freq_table(index_for_bigrams, "bigram")

    elif int(n)==3:
        # Trigram
        index_for_trigrams = inverted_index_for_trigram()
        write_inverted_index(index_for_trigrams,"trigram")
        term_freq_table_for_trigram = make_term_freq_table(index_for_trigrams, "trigram")
        doc_freq_table_for_trigram = make_doc_freq_table(index_for_trigrams, "trigram")

    else:
        print "Please enter  1 or 2 or 3"



if __name__ == "__main__": main()