from Spider import ShanbayBook
from WriteExcel import Sheet

book_id = int(input('输入book_id:'))
list_init_id = int(input('输入list_init_id:'))
list_number = int(input('输入list个数:'))
excel_name = input('输入excel表格名称，存放在当前文件夹下:')

book = ShanbayBook(book_id,list_init_id,list_number,'./word.html')
book.crawl_book()

sheet = Sheet(excel_name,book.output_location)
sheet.writeExcel()
