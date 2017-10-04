import urllib.request

def read_text():
    quotes = open('C:\\Users\\krzysiek\\Desktop\\sentence_checker\\sentence.txt')
    cont_file = quotes.read().splitlines()
    quotes.close()
    chceck_prof(cont_file)
    
def chceck_prof(text_to_check):
    for x in text_to_check:
        y = x.replace(" ", "")
        con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+y)
        out = con.read()
        if out == b'true':
            print(x+' Checking: !!!WARNING!!! - Is prof')
        else:
            print(x+' Checking: GOOD! - Is not prof')
        con.close()

read_text()
