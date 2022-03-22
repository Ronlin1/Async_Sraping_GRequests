### Importing libraries ###
import requests
import time

### Starting the timer ###
start_time = time.time()

### Our URL List ###
urls = ['https://nytimes.com',
            'https://github.com',
            'https://google.com',
            'https://reddit.com',
            'https://hashnode.com',
            'https://producthunt.com']

### Getting our Requests With ###
for link in urls:
    req = requests.get(link)
    print(f"[+] Getting Link [+] {link}  === {req} ")

### End Time ###
end_time = time.time() 
print("It took --- {} seconds --- for all the links"
      .format(end_time - start_time))