from Spider import ShanbayBook
from WriteExcel import Sheet

book = ShanbayBook(205950,643548,9,'./word.html')
book.crawl_book()

sheet = Sheet('./扇贝四级核心词汇.xls',book.output_location)
sheet.writeExcel()
