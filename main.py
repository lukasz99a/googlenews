from GoogleNews import GoogleNews
import time

tags = ["TVP", "TVP info", "Morawiecki", "Podatki", "Obostrzenia", "Policja", "Sejm", "Ekonomia", "Nauka"]

googlenews = GoogleNews(lang='pl')

def get_news(tags):
    result = []
    for tag in tags:
        print(f'getting {tag} news')
        googlenews.clear()
        googlenews.get_news(tag)
        result = result + googlenews.get_texts()
    return result

def save_news(filename, listname):
    print("saving...")
    # result_set = set(result)
    result_set = list(dict.fromkeys(listname))
    addlen = len(result_set)

    file = open(filename, 'a')
    for line in result_set:
        file.write(line + '\n')
    file.close()

    file = open(filename, 'r')
    rawlines = file.readlines()
    # print(rawlines)
    rawlen = len(rawlines)

    # cleanlines = set(rawlines)
    cleanlines = list(dict.fromkeys(rawlines))

    # print(cleanlines)
    cleanlen = len(cleanlines)

    file = open(filename, 'w')
    for line in cleanlines:
        file.write(line)
    file.close()

    print("saved")
    print(f'{rawlen} all lines')
    print(f'{addlen} lines added')
    print(f'{rawlen - cleanlen} duplicate lines removed')
    print(f'{cleanlen} unique lines')



result = get_news(tags)
save_news("news.txt", result)
# time.sleep(10000)
