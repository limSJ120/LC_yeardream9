class Crawler:
    def urllist(self, csv_file):
        with open(csv_file, 'r') as f:
            return f.read().split(',')
