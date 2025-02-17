""" 
For this homework, you will need to write a Python program 
that reads the HTML content of a web page and extracts the 
headlines and summaries of the articles on that page.

Author: Rachel Newman

Student ID: 2562294

Resources: All of the code was copied from Canvas for this assignment. I finished the regex for the get_headlines function and the 
get_summaries functions. When running the code, I realized my output didn't exactly match the one on Canvas. In an attempt to debug 
my code, I used the reference websites posted in the module for Regular Expressions, and I attempted to copy my code to ChatGPT to
figure out what I was doing wrong. ChatGPT gave me several different options for my regex in both functions, but they resulted in the 
same exact output, so I just kept what I initially put.
"""
import re
from urllib.request import Request, urlopen

"""Okay, so I fear I have incorrectly done the regex for both functions because the output doesn't exactly match the output in the
assignment instructions. I may be incorrectly pulling the headers because the output I get is a string starting with '<a href ...</a>'
for all 37 of the headers. For the summaries, all of them print out fine, but there is an extra summary that it is pulling for 
some reason (hence the output having 38 instead of 37). I am horrible at debugging code because I don't understand a lot of code, even
when I try to understand, it just flies over my head.  """

def get_headlines(html: str) -> list[str]:
    """Extracts the headlines from the HTML content"""
    h3_pattern = re.compile(r"<h3>(.*?)</h3>", re.DOTALL)
    return h3_pattern.findall(html)


def get_summaries(html: str) -> list[str]:
    """Extracts the summries from the HTML content"""
    h3_pattern = re.compile(r"<p>(.*?)</p>", re.DOTALL)
    return h3_pattern.findall(html)


if __name__ == '__main__':
    url = "https://wolfpaulus.com/posts"
    try:
        request = Request(url)
        request.add_header("User-Agent", "Mozilla/5.0")
        with urlopen(request) as page:
            text = page.read().decode('utf-8')
    except OSError as e:
        print(f"Failed to open {url}", e)
    else:
        for i, headline in enumerate(get_headlines(text), start = 1):
            print(f"{i}. {headline}")
        print("\n"+"-"*50+"\n")
        for i, summary in enumerate(get_summaries(text), start = 1):
            print(f"{i}. {summary}")