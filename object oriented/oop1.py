import datetime
time=datetime.date.today()
print(time)

#another way to show import libraries
from datetime import datetime
d=datetime.today()
print(d)

import webbrowser as wb
url='http://python.org'
wb.open(url)