import sys
import pyperclip
import urllib2
import re
import tinyurl



def url():
    """
    takes args from command line and creates
    a url. Tests url to make sure a meme is created
    if not, user is notified
    """
    if len(sys.argv) < 2:
        print "You must at least input the name of a meme"
        return False
    raw_meme_name = sys.argv[1]
    cap_meme_name = raw_meme_name.title()
    formatted_meme_text = "+".join(raw_meme_name.split())
    formatted_cap_meme_text = "+".join(cap_meme_name.split())
    if sys.argv[1] == "list":
        list_url = urllib2.urlopen("http://apimeme.com/images").read()
        list_lines = re.sub(r",","\r\n", list_url)
        print list_lines
        return False
    if len(sys.argv) >= 3:
        raw_top_text = sys.argv[2]
        formatted_top_text = "+".join(raw_top_text.split())
    else:
        formatted_top_text = ""
    if len(sys.argv) >= 4:
        raw_bottom_text = sys.argv[3]
        formatted_bottom_text = "+".join(raw_bottom_text.split())
    else:
        formatted_bottom_text = ""
    if len(sys.argv) > 4:
        print "You've added too many arguments"
        return False
    meme_url = "http://apimeme.com/meme?meme=" + formatted_meme_text + "&top=" + formatted_top_text + "&bottom=" + formatted_bottom_text
    test_url = urllib2.urlopen(meme_url).read()
    matches = re.findall('No meme found', test_url);

    if len(matches) == 0: 
       return meme_url
    else:
        meme_url = "http://apimeme.com/meme?meme=" + formatted_cap_meme_text + "&top=" + formatted_top_text + "&bottom=" + formatted_bottom_text
        test_url = urllib2.urlopen(meme_url).read()
        matches = re.findall('No meme found', test_url);
        if len(matches) == 0: 
            return meme_url
        else:
            print "That meme does not exist. Try again, or use 'list' as the only argument to show the lsit of available memes"
            return False

def shorten(address):
    """
    Creates a short url with TinyUrl
    """
    tiny = tinyurl.create_one(address)
    return tiny

def clipboard_copy(output):
    """
    Copies TinyUrl to clipboard
    """
    pyperclip.copy(output)

long_url = url()
if long_url == False:
    pass
else:
    short = shorten(long_url)
    copy_url = clipboard_copy(short)
    print "Meme url has been copied to your clipboard"