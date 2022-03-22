### Importing libraries ###
import grequests
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
our_requests = (grequests.get(link) for link in urls)
responses = grequests.map(our_requests)

for link in urls:
    for response in responses:
        print(end="")
    print(f"[+] Getting Link [+] {link}  === {response} ")

### End Time ###
end_time = time.time() 
print("It took --- {} seconds --- for all the links"
      .format(end_time - start_time))