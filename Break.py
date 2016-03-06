import time
import webbrowser
count = 0
print ('This program started on'+time.ctime())
while (count < 3):
    time.sleep(11)
    webbrowser.open("https://www.youtube.com/watch?v=lzNbGH1oZJc")
    count=count+1
