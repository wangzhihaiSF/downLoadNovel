import requests, bs4, datetime
novel = open("zhetian.txt", "a+", encoding="utf-8")
pageNumber = 404142
i = 1
print("开始下载...")
while pageNumber < 406011:
    startTime = datetime.datetime.now()
    response = requests.get("https://www.booktxt.net/1_1213/" + str(pageNumber) + ".html").content
    newResponse = bs4.BeautifulSoup(response, "html.parser")
    contentTag = newResponse.select("#content")
    for j in contentTag:
        lineContent = j.getText()
        novel.write(lineContent+"\n")
    pageNumber += 1
    endTime = datetime.datetime.now()
    consumingTime = endTime-startTime
    print("第"+str(i)+"用时："+ str(consumingTime))
    i +=1
if pageNumber == 406011:
    print("Done")
    novel.close()