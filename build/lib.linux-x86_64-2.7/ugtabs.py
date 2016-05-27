NAME = "ugtabs"
VERSION = "1.0"
AUTHOR = "Satkar Dhakal"
AUTHOR_EMAIL = "satkar@satkardhakal.com.np"
URL = "http://github.com/satcar77/ugtabs"
import os
import sys,webbrowser
import bs4,requests
import subprocess
def navigate(soup,numbers=1,typ='chords'):
	filter=[]
	c=0
	links=sort(get_me_tuple(soup))
	n=min(numbers,len(links))
	for i in links:
		if i[2]==typ or typ=="any":
			filter.append(i[1])
			c+=1
		if c>=numbers:
			break
	return filter
def browser_open(lists):
	if lists:
		print "Browser will open shortly displaying your tabs"
		for i in lists:
			webbrowser.open(i)
	else:
		print "Sorry no tabs/chords found for the song"
def console_open(lists):
	if lists:
		soup=[]
		print "Displaying the tabs in the Console... Please Wait"
		try:
			for i in lists:
				
				soup=bs4.BeautifulSoup(requests.get(i).text,"lxml")
				tabs=soup.select("pre.js-tab-content")
				if tabs:
					print tabs[0].text 
		except requests.exceptions.RequestException:
			print("Error! fetching the tabs. Please try again.")

	else:
		print "Sorry no tabs/chords found for the song"

def get_me_tuple(soup):
	print "Selecting Best Tabs/Chords for you........"
	arr=[]
	row=soup.select("tr")
	del row[0]
	for n in row:
		link=n.select("a")
		ratings=n.select(".ratdig")
		typ=n.select("td strong")
		if ratings and typ and link:
			arr.append((int(ratings[0].text.encode('utf-8')),link[0].get("href"),typ[0].text.encode('utf-8')))
	if len(arr)>2:
		del arr[0]
		del arr[0]
	return arr
def sort(arr):
	arr.sort(reverse=True)
	return arr
		
def save_to_file(title,lists):
	file=open(title+".txt",'w')
	if lists:
		soup=[]
		for i in lists:
			
			soup=bs4.BeautifulSoup(requests.get(i).text,"lxml")
			tabs=soup.select("pre.js-tab-content")
			file.write(tabs[0].text)
			file.write("\n//end--------------------------------------------------------------------------------------end//")
		print "File Successfully Saved!!!"
	else:
		print "Sorry no tabs/chords found for the song. Nothing Saved"
	file.close()

def currentlyplaying():

	artist = None
	title = None
	rhythmbox = exeexists("rhythmbox-client")
	if rhythmbox:
		output = subprocess.Popen(
				["rhythmbox-client", "--no-start", "--print-playing", 
						"--print-playing-format=%ta\n%tt"],
				stdout=subprocess.PIPE).communicate()[0]
		if len(output) > 0 and output != "Not playing\n":
			(artist, title) = output.split("\n")[0:2]
			return (artist, title)
		else:
			print"No song is playing on rhythmbox"	
			sys.exit(1)	
	else:
		print"No rhythmbox player exists"	
		sys.exit(1)	
	
def exeexists(program):
	for path in os.environ["PATH"].split(os.pathsep):
		exefile = os.path.join(path, program)
		if os.path.exists(exefile) and os.access(exefile, os.X_OK):
			return True
	return False
