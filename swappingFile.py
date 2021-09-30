def swapFileData():
    f1=open("sample1.txt")
    f2=open('sample2.txt')
    data_a=f1.read()
    data_b=f2.read()
    f1=open("sample1.txt","w")
    f2=open('sample2.txt',"w")
    f1.write(data_b)
    f2.write(data_a)

swapFileData()