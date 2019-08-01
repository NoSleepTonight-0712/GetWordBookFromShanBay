import re

import xlwt


class Sheet():
    location = ''
    source = ''
    workbook = None
    words = False
    word_sheet = None

    def __init__(self, location, source):
        self.location = location
        self.source = source
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.word_sheet = self.workbook.add_sheet('单词')

    def getword(self):
        word_pattern = re.compile('<td class="span2"><strong>.*?</strong></td>')
        with open(self.source, 'r', encoding='utf-8') as source:
            content = ' '.join(source.readlines())
            words = word_pattern.findall(content)
            for i in range(len(words)):
                words[i] = words[i].replace('<td class="span2"><strong>','').replace('</strong></td>','')
            return words

    def getExplanation(self):
        with open(self.source, 'r', encoding='utf-8') as source:
            content = ' '.join(source.readlines())
            explanation_patten = re.compile('<td class="span10">.*?</td>\n', re.DOTALL)
            explanations = explanation_patten.findall(content)
            for i in range(len(explanations)):
                explanations[i] = explanations[i].replace('<td class="span10">','').replace('</td>','')
            return explanations

    def writerow(self, row, content):
        counter = 1
        for i in range(0, len(content)):
            self.word_sheet.write(i + 1, row, content[i])
            counter += 1
            if counter > 500:
                self.workbook.save(self.location)
                counter = 1
                print('500 items have been written.')
        self.workbook.save(self.location)
        counter = 1
        print('All items have been written.')

    def writeExcel(self):
        self.writerow(0,self.getword())
        self.writerow(1,self.getExplanation())
