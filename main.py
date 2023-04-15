import os
import schedule
import time
from git import Repo
from dotenv import load_dotenv

load_dotenv()

repo = Repo(os.getcwd())

os.system("git config --global user.name %s" % os.getenv('NAME'))
os.system("git config --global user.email %s" % os.getenv('EMAIL'))
os.system("git config --global github.user %s" % os.getenv('GITHUB_USERNAME'))
os.system("git config --global github.token %s" % os.getenv('GITHUB_API_TOKEN'))
os.system("git config pull.rebase false")
os.system("git pull")
os.system("git add .")
os.system("git commit -m '🧃'")
os.system("git push")

def update():
    #Download the file
    os.system('wget https://spys.me/socks.txt -O socks.txt')

    #Open the file
    data = open('socks.txt', 'r').read()
    data = data.splitlines(True)

    #Remove the first 6 lines
    data = data[6:]

    #Version with "," at the end
    #output = [ ('\"http://' + proxy.split(' ')[0] + '\",\n') for proxy in data ]

    #Version without "," at the end
    output = [ ('\"http://' + proxy.split(' ')[0] + '\"\n') for proxy in data ]

    #Write the file
    correct = open('sources/proxy.txt', 'w').write(''.join(output[:-2]))

#schedule.every(1).minutes.do(update)

#while True:
#    schedule.run_pending()
#   time.sleep(1)


