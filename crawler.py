class Crawler:
    def __init__(self, url):
        self.url = url

    def urllist(self, csv_file):
        with open(csv_file, 'r') as f:
            return f.read().split(',')

if __name__ == "__main__":   
    url_obj = Crawler('')
    url_list = url_obj.urllist('./joseon.csv')
