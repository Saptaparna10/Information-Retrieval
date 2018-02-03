from math import log
import operator

# Global variables:
# maintains the dictionary for all the pages and their corresponding inlinks
dictionary_inlink = {}
# maintains the dictionary for all the pages and their corresponding number of outlinks
dictionary_outlink = {}
# maintains the initial page rank for all the pages
page_rank_dictionary_initial = {}
# maintains the updated page rank for all the pages
page_rank_dictionary_new = {}
# list of all the pages 
page_list = []
# list of all the pages having no outlinks
sink_page_list = []
# PageRank damping/teleportation factor
d = 0.85

# scans the given file and populates dictionaries
def scan_file(file):
    file_content = open(file, 'r')
    for line in file_content.readlines():
        words = line.split()
        make_dictionary_inlink(words)
        make_list_of_pages(words)
    make_dictionary_outlink()

# makes the dictionary of inlink pages
def make_dictionary_inlink(words):
    key = words[0]
    values = words[1:]
    dictionary_inlink[key] = values

# makes the list of all pages
def make_list_of_pages(words):
    page_list.insert(0,words[0])

# makes dictionary of outlink pages
def make_dictionary_outlink():
    for key in dictionary_inlink.keys():
        for value in dictionary_inlink[key]:
            if dictionary_outlink.has_key(value):
                dictionary_outlink[value] = dictionary_outlink[value] + 1
            else:
                dictionary_outlink[value] = 1

# initiates page rank with 1/n value
def initiate_pagerank():
    total_pages = len(page_list)
    for each_page in page_list:
        page_rank_dictionary_initial[each_page] =   float (1)/total_pages
    initiate_sink_pagelist()

# makes sink_page_list
def initiate_sink_pagelist():
    for page in page_list:
        if not dictionary_outlink.has_key(page):
            sink_page_list.insert(0,page)

# calculates the perplexity
def perplexity_calculation(dict):
    entropy = 0
    for page in page_list:
        entropy += dict[page]*log(1.0/dict[page],2)
    return 2**entropy

# calculates the page rank
def calculate_pagerank():
    counter = 0
    perplexity = 0
    iteration = 0
    initiate_pagerank()
    while(counter < 4):
        sink_page_rank = 0
        for page in sink_page_list:
            sink_page_rank = sink_page_rank + page_rank_dictionary_initial[page]
        for page in page_list:
            page_rank_dictionary_new[page] = float (1-d)/len(page_list)
            page_rank_dictionary_new[page] += d * float (sink_page_rank/len(page_list))
            for inlink_page in dictionary_inlink[page]:
                page_rank_dictionary_new[page] = page_rank_dictionary_new[page] + (d * float(page_rank_dictionary_initial[inlink_page]) / float(dictionary_outlink[inlink_page]))
        for page in page_list:
            page_rank_dictionary_initial[page] = page_rank_dictionary_new[page]
        perplexity_updated = perplexity_calculation(page_rank_dictionary_initial)
        if abs(perplexity_updated - perplexity) < 1:
            counter +=  1
        else:
            counter = 0
        perplexity = perplexity_updated
        iteration += 1
        print("Perplexity for iteration number " + str(iteration) + " is " + str(perplexity_updated))

# sorts and prints top 50 pages by their docID and PageRank Score
def sort_page_rank(dict):
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
    count = 0
    while count <50 and count < len(sorted_dict):
        print sorted_dict[count]
        count += 1

# sorts and prints top 10 pages by their docID and inlink counts
def sort_in_link(dict):
    temp_dict={}
    for page in dict.keys():
        temp_dict[page]=len(dict.get(page))
    sorted_dict = sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True)
    count = 0
    while count <10 and count < len(sorted_dict):
        print sorted_dict[count]
        count += 1

# number of pages with no in-links 
def count_sources(inlink_dict):
    counter = 0
    for page in inlink_dict.keys():
        if not inlink_dict[page]:
            counter +=1
    return counter

# main method
def main():
    filename = raw_input ('Please enter the filename ')
    #filename="G2.txt"
    scan_file(str(filename))
    calculate_pagerank()
    print "---------------------PageRank-----------------------"
    print "Top 50 pages as per PageRank scores are : "
    sort_page_rank(page_rank_dictionary_new)
    print "--------------------Top Inlink counts---------------"
    print "Top 10 pages as per in-link counts are : "
    sort_in_link(dictionary_inlink)
    print "---------------------Statistics---------------------"
    print "Total number of pages in the graph are : " + str (len(page_list))
    print "Total number of pages in the graph with no out-links (sinks) are : " + str (len(sink_page_list))
    print "Total number of pages in the graph with no in-links (sources) are : " + str (count_sources(dictionary_inlink))


if __name__ == "__main__": main()
