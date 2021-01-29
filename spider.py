from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *


class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    FinalCrawled_file = ''
    queue = set()
    FinalCrawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.FinalCrawled_file = Spider.project_name + '/FinalCrawled.txt'
        self.boot()
        self.crawl_page('poor spider', Spider.base_url)

    # before start the crawling, if not any directory and files, then please create them
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.FinalCrawled = file_to_set(Spider.FinalCrawled_file)

    # display for updates. (make some love with your end-user)
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.FinalCrawled:
            print(thread_name + ' It is happening right now ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.FinalCrawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.FinalCrawled.add(page_url)
            # call file to set and set to file fuctions
            Spider.update_files() 

    # convert byte to human readable string befor parsing to LinkFinder
    @staticmethod
    # get all of links
    def gather_links(page_url):
        # final str links on it (byte coverted to str)
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                # convert byte to str and pars to LinkFinder
                html_string = html_bytes.decode("utf-8")
            # now init the object    
            finder = LinkFinder(Spider.base_url, page_url)
            # after init, call the feed then parse all of links to LinkFinder
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            # no links to crawl
            return set()
        return finder.page_links()

    # saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.FinalCrawled):
                continue
            if Spider.domain_name != get_domain(url):
                continue
            Spider.queue.add(url)

    # just update and makes the files final
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.FinalCrawled, Spider.FinalCrawled_file)
