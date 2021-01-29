from urllib.parse import urlparse


# domain name (facebook.com)
def get_domain(url):
    try:
        results = get_subDomain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# sub domain name (www.facebook.com)
def get_subDomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
