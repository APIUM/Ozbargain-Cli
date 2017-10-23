from bs4 import BeautifulSoup
import requests
import sys
import shlex

page = requests.get("http://ozbargain.com.au")

# Create a BeatifulSoup object 
soup = BeautifulSoup(page.text, 'html.parser')

class ozb:

    def getCurrentNodes():
        # Get the titles of nodes
        nodes = []
        ozbNode = soup.findAll(class_='node node-ozbdeal node-teaser')
        for node in ozbNode:
            ozbNodeItems = node.a
            for item in ozbNodeItems:
                # Get images and titles
                prettyItem = item.prettify()
                splitItem = prettyItem.split('"', 4)

                # Put nodes away
                node = []
                node.append(splitItem[1])
                node.append(splitItem[3])
                nodes.append(node)


        return(nodes)

    def getInfo():
        print("This is the name of the script: ", sys.argv[0])
        print("Number of arguments: ", len(sys.argv))
        print("The arguments are: " , str(sys.argv))

    def getTitles(length):
        titles = []
        for x in range(length):
            titles.append(ozb.getCurrentNodes()[x][0])
        for x in range(len(titles)):
            print(titles[x])

    def getScrollTitles(length):
        titles = []
        for x in range(length):
            titles.append(ozb.getCurrentNodes()[x][0])
        if length > 1:
            for x in range(len(titles)):
                print(titles[x],end="")
                if x != len(titles)-1:
                    print(" --- ",end="")
        else:
            for x in range(len(titles)):
                print(titles[x])

        



if __name__ == "__main__":
    
    # Splits and cleans up the argv line
    argv = shlex.split(str(sys.argv))
    for x in range(len(argv)):
        argv[x] = argv[x].replace(",","").replace("]","").replace("[","")
 

    if argv[1] == "-h":
        print("""
        You have reached the help file. 
        This is a script to get the nodes from the current front page of Ozbargain. 

        Options:
        -h: Show this page.
        -i: Show the info for the current script instance
        -n: Returns a list of the current nodes
        -t: Returns titles of current front page nodes in a list
                Accepts a second option, number of titles to return
                By default this is all on front page.
        -s: Returns titles on one line seperated by " --- "
                Accepts same options as -t
        """)

    if argv[1] == "-info" or argv[1] == "-i":
        ozb.getInfo()

    if argv[1] == "-n" or argv[1] == "-nodes":
        ozb.getCurrentNodes()

    if argv[1] == "-t" or argv[1] == "-titles":
        try:
            ozb.getTitles(int(argv[2]))
        except:
            ozb.getTitles(len(ozb.getCurrentNodes()))

    if argv[1] == "-s" or argv[1] == "-scroll":
        try:
            ozb.getScrollTitles(int(argv[2]))
        except:
            ozb.getScrollTitles(len(ozb.getCurrentNodes()))
