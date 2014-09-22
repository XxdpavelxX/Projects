__author__ = 'xxdpavelxx'
import re
text = ["Hello I am Jo89e I like to 234 on tO the@4! bea*%)", "oops I meant beatch.", "Today 2356", "*@#$ is", "a good5", "da2te", "to@5morow it", "not", "234567489123", \
       "u'/Archives/edgar/data/1166559/000104746907006532/0001047469-07-006532.txt'", "u'/Archives/edgar/data/1166559/000104746907006532/a2179397z13f-hr.txt"]
text2 = ' '.join(text)
match = re.findall(r'u[\D]{22}[0-9]+/[0-9]+/[0-9]+-[0-9]+-[0-9]+.txt[\D]', text2)
print match