import requests
from random import randint
from time import sleep

site = raw_input("Please specify the Parent domain: ")

print "Script is preparing the dorks to enumerate the sub-domain"
print "............................."
print "............................."
print "Script takes approximately 5 minutes to complete. In the mean time have a sip of coffee :)"

#Initalize with simple Dorks
z = "site:*." + site + " " + "-www"
#print z
row = 0
newlist = list()
urls = set()
#url
url = 'http://www.google.com/search'

#Setting User-Agent
my_headers = { 'User-agent' : 'Mozilla/11.0' }

#Parser for google.com
if ("google.com" in site):

    for i in range (20):
        #setting up the payload
        payload = { 'q' : z }

        sleep(randint(10,20))

        #Getting the response in an Object r
        r = requests.get( url, params = payload, headers = my_headers )
        #print r.status_code
        a = r.text
        #Parser for Google.com
        p = a.split()
        for i in p:
            if("http" in i):
                a = i.split(";")
                for i in a:
                    if("://" in i):
                        b = i.split(";")
                        for i in b:
                            if("site" in i):
                                c = i.split(":")
                                for i in c:
                                    d = i.split("/")
                                    for i in d:
                                        if ("google" in i):
                                            if not ("*" in i):
                                                if not ("googleusercontent" in i):
                                                    if not ("www" in i):
                                                        e = i.split(".")
                                                        for i in e:
                                                            if i != "" :
                                                                newlist = e[0]
                                                                urls.add(newlist)
                                                        
        i = 0
        for e in urls:
            a = []
            a = list(urls)[i]
            z = z + " " + "-" + str(a)
            i = i + 1
        output = []
        for x in z.split(" "):
            if x not in output:
                output.append(x)

        z = " ".join(output)

#Parser for other sites    

else:
    for i in range(10):
    
        #setting up the payload
        payload = { 'q' : z }

        sleep(randint(10,15))
    
        #Getting the response in an Object r
        r = requests.get( url, params = payload, headers = my_headers )
        #print r.status_code

        a = r.text.encode('utf-8')



        #Parser for other sites
        p = a.split()
        for i in p:
            if("http" in i):
                t = i.split(";")
                for j in t:
                    if(site in j):
                        c = j.split(":")
                        for k in c:
                            if (site and "//" in k):
                                d = k.split(",")
                                for l in d:
                                    if not ("google" in l):
                                        e = l.split("//")
                                        for m in e:
                                            if not ("www" in m):
                                                f = m.split(".")
                                                for i in f:
                                                    if i != "" :
                                                        newlist = f[0]
                                                        #print newlist
                                                        urls.add(newlist)
                                                
    #print urls                                                

        i = 0
        for e in urls:
            a = []
            a = list(urls)[i]
            z = z + " " + "-" + str(a)
            i = i + 1
        output = []
        for x in z.split(" "):
            if x not in output:
                output.append(x)

        z = " ".join(output)



print "The subdomains are as follows: \n"

i = 0
for p in urls:
    a = []
    a = list(urls)[i]
    print str(a)
    i = i + 1

print "+++++++++++++++++++++++++++++++++++++++++"
print "+++++++++++++++++++++++++++++++++++++++++"
print "+++Output will be printed out shortly++++"
print "+++++++++++++++++++++++++++++++++++++++++"
print "The last dork used was : " + z  + "\n"
print "-----------------------------------------"
print "-----------------------------------------"
print "For accurate results please manually copy paste the last dork displayed above in google search engine after few minutes."    
    
