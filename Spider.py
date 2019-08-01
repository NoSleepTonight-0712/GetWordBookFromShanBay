import requests
from bs4 import BeautifulSoup
# https://www.shanbay.com/wordlist/6091/43270/
# https://www.shanbay.com/wordlist/6091/43270/?page=2

class ShanbayBook():
    book_id=0
    list_init_id=0
    list_num=0
    output_location = ""
    def __init__(self,book_id,list_init_id,list_num,output_location):
        ''' https://www.shanbay.com/wordlist/182470/515083/
            :param book_id 如上例，为182470
            :param list_init_id 如上例，为515083
            :param list_num 如上例，点进去看有9个单元，即为9
            :param output_location 输出位置
        '''
        self.book_id=book_id
        self.list_init_id=list_init_id
        self.list_num = list_num
        self.output_location = output_location


    def crawl_page(self,list,page):
        return requests.get(self.getListUrl(list+1,page+1)).text # +1方便用range()

    def crawl_book(self,location='./word.html'):
        with open(self.output_location,'w',encoding='utf-8') as f:
            for list in range(self.list_num):
                for page in range(10):
                    content = str(BeautifulSoup(self.crawl_page(list,page),'html.parser')\
                        .find_all('table',{'class':"table table-bordered table-striped"}))
                    f.write(content)


    def getListUrl(self,list,page):
        '''
            :param list 第几个单元
            :param page 这个单元的第几页
            :return URL
        '''
        list_id = self.list_init_id+(list-1)*3
        if page==1:
            return "https://www.shanbay.com/wordlist/{}/{}/".format(self.book_id,list_id)
        else:
            return "https://www.shanbay.com/wordlist/{}/{}/?page={}".format(self.book_id,list_id,page)
