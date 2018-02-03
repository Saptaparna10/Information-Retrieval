import time
import urllib2
import re
import traceback
from bs4 import BeautifulSoup

#Global Variables:
#MAX_DEPTH indicates the maximum level till the crawler will crawl.
#The seed has depth value 1
MAX_DEPTH = 6
#Max number of  unique pages to crawl
MAX_PAGES = 1000
#FILE_INDEX stores the index of the files starting from 1 till 1000(at most)
#The first file is named as file_1, file_2... file_n
FILE_INDEX = 1
#This maps file names to respective urls
FILE_URL_MAP = { }

# breadth-first algorithm
def web_spider(seed_url):
    to_crawl = [seed_url]
    already_crawled = []
    next_depth = []
    depth = 1
    while to_crawl and len(already_crawled) < MAX_PAGES and depth <= MAX_DEPTH:
        current_page=to_crawl.pop(0)
        if current_page not in already_crawled:
            #politeness policy of 1 second
            time.sleep(1)
            urls = get_urls(current_page)
            merge(next_depth,urls)
            already_crawled.append(current_page)
            if not to_crawl:
                to_crawl, next_depth = next_depth, []
                print "Depth reached "
                print depth
                depth = depth + 1

    return already_crawled


def merge(first_list, second_list):
    for element in second_list:
        if element not in first_list:
            first_list.append(element)


def write_contents(page, html_content):
    global FILE_INDEX
    filename= 'file_' + str(FILE_INDEX) + '.txt'
    file_content = open(filename, 'w')
    file_content.write(page + "\n" + html_content)
    global FILE_URL_MAP
    FILE_URL_MAP.update({'"'+filename+'"' : '"'+page+'"'})
    file_url_list= open('crawled_urls.txt', 'a')
    file_url_list.write(str(FILE_INDEX) + "." + " "+ page + "\n")
    FILE_INDEX +=1
    file_content.close()
    file_url_list.close()


def get_urls(page):
    list_url=[ ]
    base_url = "https://en.wikipedia.org"
    try:
        handle= urllib2.urlopen(page)
        soup=BeautifulSoup(handle, "html.parser")
        write_contents(page, soup.prettify().encode("utf-8"))
        data = soup.findAll('div', attrs={'id':'bodyContent'})
        for div in data:
            for link in div.findAll('a',{'href' : re.compile('^/wiki/')}):
                href = link.get('href')
                #skipping administrative pages
                if ':' in href:
                    continue
                #url = base_url + extension
                url = base_url + href
                # Handling urls having '#'
                if '#' in url:
                    url = url[:url.index('#')]
                list_url.append(url.encode("utf-8"))
    except:
        print "Error in try block of get_urls!"
        print traceback.format_exc()
    return list_url

#main method
def main():
    print "Started crawling with seed url " + "https://en.wikipedia.org/wiki/Tropical_cyclone"
    #calling the web_spider
    my_list = web_spider("https://en.wikipedia.org/wiki/Tropical_cyclone")
    #printing the list of urls, crwaled
    print my_list
    #printing the map of file name and their URL
    print FILE_URL_MAP


if __name__ == "__main__": main()
