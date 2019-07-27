import csv


def open_logfile(filename_log):
   file=open(filename_log,'r')
   for line in file:
      yield line


if __name__=="__main__":
   csvfile=open("Report_log.csv",'w',newline='')
   fieldname=['IP','TimeStamp','HTTP Verb','Response code','URL']
   writer=csv.DictWriter(csvfile,fieldnames=fieldname)
   writer.writeheader()
   line=open_logfile("test.log")
   while True:
      str1=line.__next__()
      print(str1)
      try:
         URL="http://"+str1.split('http://')[1].split(' ')[0]
      except Exception as e:
         URL="http://"+str1.split('- -')[0]
      writer.writerow({'IP':str1.split('- -')[0],'TimeStamp':str1.split(']')[0].split('[')[1],'HTTP Verb':str1.split(']')[1].split('/')[0].strip(),'Response code':str1.split('HTTP/')[1].split(' ')[1],'URL':URL})
   csvfile.close()
   line.close()

      
   

  