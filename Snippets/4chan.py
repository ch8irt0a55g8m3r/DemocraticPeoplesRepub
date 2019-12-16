import requests
import pprint
import time
import twint


def get_boards(board):
    r = requests.get("https://a.4cdn.org/" + board + "/threads.json",
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)
    return r.json()


#  pprint.pprint(get_boards('v'))  # Get the first post and its comment
page_number = 5
threadlist = get_boards('v')[page_number - 1]["threads"]
threads = [r.get('no') for r in threadlist]
for r in threads:
    j = requests.get("https://a.4cdn.org/" + 'v' + "/thread/" + str(r) + ".json",
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)
    pprint.pprint(j.json())
    time.sleep(1.25)

# pprint.pprint(get_boards('v'))


# pprint.pprint(threadlist)

