
from ast import Raise
from multiprocessing.sharedctypes import Value
from urllib.request import urlopen		
from urllib.error import HTTPError
from urllib.error import URLError
import re
url = input("Give a valid url: ")


try:
    with urlopen(url) as f:
        data = f.read()
        s = data.decode("utf-8")
        
        
        danger = len(re.findall(r"(?:^|\b)(bomb|kill|murder|terror|terrorist|terrorism)(?:$|\b)", s))
        print("Number of dangerous words:", danger)
        
        
        
        file_name = input("Give me a valid path to save the contents? ")
        with open(file_name, "w") as f:
            f.write(s)
            f.close()
        print("Saving succeeded to: ", file_name)

except UnicodeDecodeError:
    try:
        print("Doesn't appear to be an HTML file with utf-8 encoding.")
        with urlopen(url) as f:
            data = f.read()
            file_name = input("Give me a valid path to save the contents? ")
            with open(file_name, "wb") as out_file:
                out_file.write(data)
            print("Saving succeeded to: ", file_name)
    except FileNotFoundError:
        print("Saving Failed")
    
        

except ValueError:
    print("Not URL ", url) 

except FileNotFoundError:
    print("Saving Failed")

except HTTPError:
    print("Error opening url: ", url)    
except  URLError:
    print("Error opening url: ", url)    






    



