import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
  print("There was a problem: %s" % (exc))
#The raise_for_status() method is a good way to ensure that a program
#halts if a bad download occurs. This is a good thing: You want your program
#to stop as soon as some unexpected error happens. If a failed download isn’t
#a deal breaker for your program, you can wrap the raise_for_status() line
#with try and except statements to handle this error case without crashing.
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
