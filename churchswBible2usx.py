'''
Takes a bible xml file found on the churchsw.org website and converts into .usx format
'''

import codecs
import xml.etree.ElementTree as et

f = codecs.open("Bible.xml", mode='r')
tree = et.parse(f)
root = tree.getroot()

def findCode(bname):
    bkCode = {'Genesis':'GEN', 'Exodus':'EXO', 'Leviticus':'LEV', 'Numbers':'NUM', 'Deuteronomy':'DEU', 'Joshua':'JOS', 'Judges':'JDG', 'Ruth':'RUT', '1 Samuel':'1SA', '2 Samuel':'2SA', '1 Kings':'1KI', '2 Kings':'2KI', '1 Chronicles':'1CH', '2 Chronicles':'2CH', 'Ezra':'EZR', 'Nehemiah':'NEH', 'Esther':'EST', 'Job':'JOB', 'Psalms':'PSA', 'Psalm':'PSA', 'Proverbs':'PRO', 'Ecclesiastes':'ECC', 'Song of Songs':'SNG', 'Song of Solomon':'SNG', 'Isaiah':'ISA', 'Jeremiah':'JER', 'Lamentations':'LAM', 'Ezekiel':'EZK', 'Daniel':'DAN', 'Hosea':'HOS', 'Joel':'JOL', 'Amos':'AMO', 'Obadiah':'OBA', 'Jonah':'JON', 'Micah':'MIC', 'Nahum':'NAM', 'Habakkuk':'HAB', 'Zephaniah':'ZEP', 'Haggai':'HAG', 'Zechariah':'ZEC', 'Malachi':'MAL', 'Matthew':'MAT', 'Mark':'MRK', 'Luke':'LUK', 'John':'JHN', 'Acts':'ACT', 'Romans':'ROM', '1 Corinthians':'1CO', '2 Corinthians':'2CO', 'Galatians':'GAL', 'Ephesians':'EPH', 'Philippians':'PHP', 'Colossians':'COL', '1 Thessalonians':'1TH', '2 Thessalonians':'2TH', '1 Timothy':'1TI', '2 Timothy':'2TI', 'Titus':'TIT', 'Philemon':'PHM', 'Hebrews':'HEB', 'James':'JAS', '1 Peter':'1PE', '2 Peter':'2PE', '1 John':'1JN', '2 John':'2JN', '3 John':'3JN', 'Jude':'JUD', 'Revelation':'REV'}
    return bkCode[bname]


o = codecs.open('HOV.usx', 'w', 'utf-8')
o.write('<?xml version="1.0" encoding="utf-8"?>\n<usx version="2.0">\n') 
for bk in root.iter('BIBLEBOOK'):
    bkCode = findCode(bk.attrib['bname'])
    o.write('<book code="' + bkCode +'" style="id" />\n')
    for ch in bk.iter('CHAPTER'):
        o.write('<chapter number="'+ ch.attrib['cnumber'] +'" style="c" />\n')
        for v in ch.iter('VERS'):
            try:
                o.write('<para style="p">\n<verse number=' + v.attrib['vnumber'] + '" style="v" />'+v.text+'\n</para>')
            except TypeError:
                o.write('<para style="p">\n<verse number=' + v.attrib['vnumber'] + '" style="v" />'+'No verse text\n')                
o.close()
f.close()
