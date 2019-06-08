
fw = open('simple.txt','w')

fw.write('love you \n')
fw.write('i love python \n')
fw.close()

fr = open('simple.txt','r')
text = fr.read()
print(text)

fr.close()