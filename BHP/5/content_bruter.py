#!/usr/bin/env python3

import queue
import threading
import urllib.error
import urllib.parse
import urllib.request

threads = 50
target_url = "http://locahost/"
wordlist_file = "wordlist.txt"
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) " \
             "Gecko/201100101 " \
             "Firefox/19.0"

def build_wordlist(wordlist_file):
    # read in the wordlist
    fd = open(wordlist_file, "r")
    raw_words = [line.rstrip('\n') for line in fd]
    fd.close()

    found_resume = False
    words = queue.Queue()

    for word in raw_words:
        if resume:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist from: %s" % resume)
        else:
            words.put(word)
    return words

def dir_bruter(extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []

        # check if there is a fiel extension if not
        # it's a diretory path we're bruting
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)

        # if we wantt to bruteforce extensions
        if extensions:
            for extension in extensions:
                attempt_list.appen("/%s%s" % (attempt, extension))

        # iterate over our list of attempts
        for brute in attempt_list:
            url = "%s%s" % (target_url, urllib.parse.quote(brute))
            try:
                headers = {"User-Agent": user_agent}
                r = urllib.request.Request(url, headers=headers)
                response = urllib.request.urlopen(r)
                if len(response.read()):
                    print("[%d] => %s" % (response.code, url))
            except urllib.error.HTTPError as e:
                if e.code != 404:
                    print("!!! %d => %s" %(e.code, url))
                pass

word_queue = build_wordlist(wordlist_file)
file_extensions = [".php", ".bck", ".orig", ".inc"]

for i in range(threads):
    t = threading.Thread(target=dir_bruter, args=(file_extensions,))
    t.start()

