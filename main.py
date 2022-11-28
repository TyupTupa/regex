import urllib.request
import re


def get_info_from_url(url):
    with urllib.request.urlopen(url) as resp:
        html = resp.read()
        file = html.decode("utf8")
        # f = open('file.html','w')
        # f.write(file)
        # f.close()
        return file


def regex(file):
    reg_link = r"[\"\']https?\:\/\/[^\"\']*[\"\']"
    reg_file = r"(?<=\w\/)[^\/\\\n:\*\?\<\>|\+]+\.[a-zA-Z]{1,4}(?=[\?\/\"\'])"
    result_links = re.findall(reg_link, file)
    # print(result_links)
    result = []
    for link in result_links:
        print(link, re.findall(reg_file, link))
        result += re.findall(reg_file, link)
    return result


url = 'https://edu.stankin.ru/'

file = get_info_from_url(url)
result = regex(file)

for cur_file in result:
    print(cur_file)
