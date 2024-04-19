import csv

class Crawler:
    def __init__(self, url):
        self.url = url

    def urllist(self, csv_file):
        urls = []
        with open(csv_file, 'r') as f:
            rdr = csv.reader(f)
            for line in rdr:
                url = line[0]
                urls.append(Crawler(url))
        return urls
if __name__ == "__main__":   
    url_obj = Crawler('')
    url_list = url_obj.urllist('./joseon.csv')

for url_link in url_list:
    print(url_link.url)
