import csv

def open_log_csv(filename_csv):
      csvfile=open(filename_csv,'w')
      fieldname=['IP','TimeStamp','HTTP Verb','Response Code','URL']
      writer=csv.DictWriter(csvfile,fieldnames=fieldname)
      writer.writeheader()
      yield writer

def open_logfile(filename_log):
   file=open(filename_log,'r')
   for line in file:
      yield line

def prepare_csv(filename_log,filename_csv):
    log_file_line_gen=open_logfile(filename_log)
    csv_file_gen=open_log_csv(filename_csv).__next__()
    while True:
         try:
             line=log_file_line_gen.__next__()
             try:
                  URL="http://"+line.split('http://')[1].split(' ')[0]
             except:
                  URL="http://"+line.split('- -')[0]
             csv_file_gen.writerow({'IP':line.split('- -')[0],'TimeStamp':line.split(']')[0].split('[')[1],'HTTP Verb':line.split(']')[1].split('/')[0].strip(),'Response Code':line.split('HTTP/')[1].split(' ')[1],'URL':URL})
         except StopIteration as s:
               break

if __name__=="__main__":
    prepare_csv("test.log","Request.csv")
   
