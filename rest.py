import time
import webbrowser

break_count = 0

ask = int(input("How many minutes do you want to take then go for a  break??"))
total_break = int(input("number of times to go for break?"))
while (break_count < total_break):
        print("I started breaking at " + time.ctime())
        time.sleep(60*ask)
        #you can provide url if needed to video you want online or path to song you want on local machine as below
        webbrowser.open(r"C:\Users\proud\Desktop\song\khallid_dumb_and_broke.MKV")
        break_count = break_count + 1

    
