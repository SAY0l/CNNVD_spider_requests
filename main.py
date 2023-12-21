from cli.cli import *

class App:
    Description = "CNNVD_spider_requests: Crawl CNNVD Data Rapidly"
    Author = "sayol"
    Email = "github@sayol.com"
    Verion ="1.0"
    Ps = ">>> u must indicate start_page and end_page <<<"

    def __init__(self) :
        Gen_cli([self.Description, self.Author, self.Email, self.Verion,self.Ps])


if __name__ == "__main__":
    start = App()