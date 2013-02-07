import urllib2, logging

def get_URL(url):
    try:
        response = urllib2.urlopen(req)
        return response
    except urllib2.URLError, e:
        if hasattr(e,'reason'):
            logging.warning('urlopen() returned error %s\n',e.reason)
        elif hasattr(e,'code'):
            logging.warning('Server couldn\'t fulfill request: %s\n',e.code)
        else:
            logging.warning('Opened %s with response code %s',url,response.getcode())

def parse(url):
    logging.info('Getting URL %s', url)
    try:
        response = get_URL(urllib2.urlopen(request))
        soup = BeautifulSoup(response)
    except:
        logging.error('Error parsing %s',url)
        return
    return soup

def get_XML(url):
    try:
        request = get_URL(url)
    except Exception as e:
        logging.error('Could not open URL %s (%s)', url, e)
        return

    try:
       tree = ET.parse(req) 
    except Exception as e:
        logging.error('Could not parse XML at %s (%s)', url, e)
        return

    return tree
