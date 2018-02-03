import io
import glob
import operator
import os
import traceback
from pprint import pprint
from math import sqrt
from math import log


CURRENT_DIRECTORY = os.getcwd()
# Path of corpus
INPUT_FOLDER = path = os.path.join(CURRENT_DIRECTORY,'corpus')
# Path where BM25 scores will be stored 
OUTPUT_FOLDER_PATH = path = os.path.join(CURRENT_DIRECTORY,'doc_score_BM25')
DOC_NAME ={} # mapping doc name and ids
QUERY_ID = 0
AVDL = 0 # Average doc length
number_of_Token = {}

# Inverted index for unigram
def inverted_index_for_unigram():
    # term -> (docid,tf)
    inverted_index = {}
    # docid -> tf
    doc_id_tf_dict = {}
    #number_of_Token = {}
    try:
        doc_count=1
        path = os.path.join(CURRENT_DIRECTORY,'corpus')
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
                doc_count = doc_count + 1
            f.close()
        print "toeken count : " 
        print number_of_Token
        total_num_of_docs = doc_count-1
    except:
        print "Error in try block of inverted_index_for_unigram!"
        print traceback.format_exc()
    return inverted_index,total_num_of_docs


#--------------------------------------------------------------------#
#-------------------------HW3 Indexer functions----------------------#
#--------------------------------------------------------------------#
# def make_term_freq_table(inverted_index,ngram):

#     term_frequency = {}
#     for term in inverted_index:
#         frequency = 0
#         doc_id_tf_dict = inverted_index[term]
#         for doc_id in doc_id_tf_dict:
#             frequency = frequency + doc_id_tf_dict[doc_id]
#         term_frequency[term] = frequency
#     sorted_term_frequency = sorted(term_frequency.items(), key=operator.itemgetter(1), reverse=True)
#     write_term_frequency_to_file(sorted_term_frequency,ngram)
#     return sorted_term_frequency


# def write_term_frequency_to_file(term_frequency,ngram):

#     try:
#         print "Writing term frequency table..."
#         file_name= "term_frequency" + "_" + str(ngram) + ".txt"
#         file_term_frequency= open(file_name, 'w')
#         table_form = '{:<30}' * 2
		
#         for term in term_frequency:
#             file_term_frequency.write(table_form.format(str(term[0]),str(term[1])))        
#             file_term_frequency.write("\n")
#         file_term_frequency.close()
#     except:
#         print "Error in try block of write_term_frequency_to_file!"
#         print traceback.format_exc()

# def make_doc_freq_table(inverted_index,ngram):
#     document_freq = {}

#     for term in inverted_index:
#         document_list = []
#         doc_dict = inverted_index[term]
#         for doc_id in doc_dict:
#             document_list.append(doc_id)
#         document_freq[term] = document_list

#     sorted_document_freq = sorted(document_freq.items(), key=operator.itemgetter(0))
#     write_document_freq(sorted_document_freq, ngram)
#     return sorted_document_freq

# # generates file with doc frequency table
# def write_document_freq(document_freq, ngram):

#     try:
#         print "Writing document frequency table..."
#         file_name= "doc_freq_table" + "_" + str(ngram) + ".txt"
#         file_doc_freq_table= open(file_name, 'w')
#         for list in document_freq:
#             table_form_doc = '{:<10}' * 3
#             list_length = len (list[1])
#             file_doc_freq_table.write(table_form_doc.format((str(list[0])),(str(list[1])),(str(list_length))))
#             file_doc_freq_table.write("\n")
#         file_doc_freq_table.close()
#     except:
#         print "Error in try block of write_doc_freq!"
#         print traceback.format_exc()



# def inverted_index_for_bigram():

#     # term -> (docid,tf)
#     inverted_index = {}
#     # docid -> tf
#     doc_id_tf_dict = {}
#     number_of_Token = {}
#     try:
#         directory_name = os.getcwd()
#         path = os.path.join(directory_name,'corpus')
#         for filename in glob.glob(os.path.join(path, '*.txt')):
#             with file(filename) as f:
#                 document =f.read()
#                 file_name = str(filename).split ('corpus\\')[1][:-4]
#                 print "Generating index for " + file_name
#                 words = document.split()
#                 number_of_Token[file_name] = len(words)-1
#                 for i in range(len(words) - 1) :
#                     word = words[i] + " " + words[i+1]
#                     if not inverted_index.has_key(word):
#                         doc_id_tf_dict = {file_name : 1}
#                         inverted_index[word] =  doc_id_tf_dict
#                     elif inverted_index[word].has_key(file_name):
#                         doc_id_tf_dict = inverted_index[word]
#                         value = doc_id_tf_dict[file_name]
#                         value = value + 1
#                         doc_id_tf_dict[file_name] = value
#                     else:
#                         doc_id_tf_dict = {file_name : 1}
#                         inverted_index[word].update(doc_id_tf_dict)
#             f.close()
#         print "toeken count : " 
#         print number_of_Token


#     except:
#         print "Error in try block of inverted_index_for_unigram!"
#         print traceback.format_exc()
#     return inverted_index

# def inverted_index_for_trigram():

#     # term -> (docid,tf)
#     inverted_index = {}
#     # docid -> tf
#     doc_id_tf_dict = {}
    
#     try:
#         directory_name = os.getcwd()
#         path = os.path.join(directory_name,'corpus')
#         for filename in glob.glob(os.path.join(path, '*.txt')):
#             with file(filename) as f:
#                 document =f.read()
#                 file_name = str(filename).split ('corpus\\')[1][:-4]
#                 print "Generating index for " + file_name
#                 words = document.split()
#                 number_of_Token[file_name] = len(words)-2
#                 for i in range(len(words) - 2) :
#                     word = words[i] + " " + words[i+1] + " " + words[i+2]
#                     if not inverted_index.has_key(word):
#                         doc_id_tf_dict = {file_name : 1}
#                         inverted_index[word] =  doc_id_tf_dict
#                     elif inverted_index[word].has_key(file_name):
#                         doc_id_tf_dict = inverted_index[word]
#                         value = doc_id_tf_dict[file_name]
#                         value = value + 1
#                         doc_id_tf_dict[file_name] = value
#                     else:
#                         doc_id_tf_dict = {file_name : 1}
#                         inverted_index[word].update(doc_id_tf_dict)
#             f.close()
#         print "toeken count : " 
#         print number_of_Token


#     except:
#         print "Error in try block of inverted_index_for_unigram!"
#         print traceback.format_exc()
#     return inverted_index

# # generates file with doc frequency table
# def write_inverted_index(inverted_index, ngram):

#     try:
#         print "Writing inverted index..."
#         file_name= "inverted_index" + "_" + str(ngram) + ".txt"

#         with open(file_name, 'wt') as out:
#             pprint(inverted_index, stream=out)
          
#     except:
#         print "Error in try block of write_doc_freq!"
#         print traceback.format_exc()


#--------------------------------------------------------------------#
#--------------------HW4 Retrival Model logic------------------------#
#--------------------------------------------------------------------#
def calculate_avdl():
    try:
        sum = 0
        for doc_id in number_of_Token:
            sum+=number_of_Token[doc_id]
        return (float(sum)/float(len(number_of_Token)))
    except Exception as e:
        print(traceback.format_exc())

def calculate_doc_bm25_score(query,inverted_index,total_num_of_docs):
    try:
        query_term_freq = {}
        query_term_list = query.split()
        updated_inverted_index = {} 
        for query_term in query_term_list:
            if not query_term_freq.has_key(query_term):
                query_term_freq.update({query_term:1})
            else:
                query_term_freq[query_term]+=1
        #reducing the inverted_index with only required terms in query
        for query_term in query_term_freq:
            if inverted_index.has_key(query_term):
                updated_inverted_index.update({query_term:inverted_index[query_term]})
            else:
                updated_inverted_index.update({query_term:{}})
        calculate_score(query,query_term_freq,updated_inverted_index,total_num_of_docs)
    except Exception as e:
        print(traceback.format_exc())

def calculate_score(query,query_term,inverted_index,N):
    doc_score={}
    R = 0  # Assuming no relevance info is available
    try:
        for term in inverted_index: # inverted_index.keys() and query_term.keys() are same
            n = len(inverted_index[term])
            dl = 0
            qf = query_term[term]
            r = 0 # Assuming no relevance info is available
            for doc_id in inverted_index[term]:
                f = inverted_index[term][doc_id]
                if number_of_Token.has_key(doc_id):
                    dl = number_of_Token[doc_id]
                score = calculate_BM25(n, f, qf, r, N, dl,R)
                if doc_id in doc_score:
                    total_score = doc_score[doc_id] + score
                    doc_score.update({doc_id:total_score})
                else:
                    doc_score.update({doc_id:score})
        sorted_doc_score = sorted(doc_score.items(), key=operator.itemgetter(1), reverse=True)
        write_doc_score_to_file(query,sorted_doc_score)
    except Exception as e:
        print(traceback.format_exc())

# Writing score to individual files for each query
def write_doc_score_to_file(query,sorted_doc_score):
    try:
        if not os.path.exists(OUTPUT_FOLDER_PATH):
            os.mkdir(OUTPUT_FOLDER_PATH)             
        if(len(sorted_doc_score)>0):
            out_file  = open(OUTPUT_FOLDER_PATH +"\\"+query[:-1]+".txt",'a+')
            for i in range(min(100,len(sorted_doc_score))):
                doc_id,doc_score = sorted_doc_score[i]
                out_file.write(str(QUERY_ID) + " Q0 "+ doc_id +" " + str(i+1) + " " + str(doc_score) +" BM25_Model\n")            
            out_file.close()
            print "\nDocument Scoring for Query id = " +str(QUERY_ID) +" has been generated inside BM25_doc_score.txt"
        else:
            print "\nTerm not found in the corpus"
    except Exception as e:
        print(traceback.format_exc())

# BM25 score calculation
def calculate_BM25(n, f, qf, r, N, dl,R):
    try:
        k1 = 1.2
        k2 = 100
        b = 0.75
        K = k1 * ((1 - b) + b * (float(dl) / float(AVDL)))
        first = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
        second = ((k1 + 1) * f) / (K + f)
        third = ((k2 + 1) * qf) / (k2 + qf)
        return first * second * third
    except Exception as e:
        print(traceback.format_exc())


# main function
def main():
    global QUERY_ID,AVDL
    #generating inverted_index for unigrams
    index_for_unigrams,total_num_of_docs  = inverted_index_for_unigram()
    AVDL = calculate_avdl()
    print "avdl "
    print AVDL
    # Deleting existing files
    if os.path.exists(OUTPUT_FOLDER_PATH+"\\BM25_doc_score.txt"):
        os.remove(OUTPUT_FOLDER_PATH+"\\BM25_doc_score.txt")
    query_file = open("query.txt", 'r')
    for query in query_file.readlines():
        QUERY_ID+=1
        calculate_doc_bm25_score(query,index_for_unigrams,total_num_of_docs)
    
    # ------------------------INVERTED INDEX for n gram---------------------------------------#
           
    # n = raw_input ('Please enter value of n for n-grams...')

    # if int(n)==1:
    #     # Unigram
    #     index_for_unigrams = inverted_index_for_unigram()
    #     write_inverted_index(index_for_unigrams,"unigram")
    #     term_freq_table_for_unigram = make_term_freq_table(index_for_unigrams, "unigram")
    #     doc_freq_table_for_unigram = make_doc_freq_table(index_for_unigrams, "unigram")

    # elif int(n)==2:
    #     # Bigram
    #     index_for_bigrams = inverted_index_for_bigram()
    #     write_inverted_index(index_for_bigrams,"bigram")
    #     term_freq_table_for_bigram = make_term_freq_table(index_for_bigrams, "bigram")
    #     doc_freq_table_for_bigram = make_doc_freq_table(index_for_bigrams, "bigram")

    # elif int(n)==3:
    #     # Trigram
    #     index_for_trigrams = inverted_index_for_trigram()
    #     write_inverted_index(index_for_trigrams,"trigram")
    #     term_freq_table_for_trigram = make_term_freq_table(index_for_trigrams, "trigram")
    #     doc_freq_table_for_trigram = make_doc_freq_table(index_for_trigrams, "trigram")

    # else:
    #     print "Please enter  1 or 2 or 3"



if __name__ == "__main__": main()