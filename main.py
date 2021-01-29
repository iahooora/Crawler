import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'par'
HOMEPAGE = 'http://par.ir'
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/FinalCrawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# create mutiple threads (till jobs done)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each links in queue are a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# check the waiting list and if any link on it, do crawl all of them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue right now')
        create_jobs()


create_workers()
crawl()
