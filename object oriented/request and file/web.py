import requests
import os
import webbrowser as wb

  # when we use os that's mean we directly go the site.but when we just use requests we can 
  # save this file in own pc.  

# url='http://dimikcomputing.com'
# res=requests.get(url)

# with open('first_dimik.html','w',encoding=res.encoding) as fl:
#     fl.write(res.text)
# fl_path=os.path.realpath('first_dimik.html')
# print(fl_path)
# wb.open('file://'+fl_path)
# print(fl)

        #another task

response=requests.get('http://programiz.com')
with open('programiz.html','w',encoding=response.encoding) as f:
    f.write(response.text)
path=os.path.relpath('programiz.html')
wb.open(path)
print(path)