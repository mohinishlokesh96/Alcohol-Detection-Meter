import re
check="This is bar"
check2="Here is a Pub & Bar"
check1="R\.R\. BAR"

m=re.findall("[Bb][Aa][Rr]|[Pp][uU][bB]",check2)

print m
