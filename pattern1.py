import re

check="This is bar"

check2="Here is a Pub & Bar"

check1="This is a house"



m=re.findall("[Bb][Aa][Rr]|[Pp][uU][bB]",check1)



print m
