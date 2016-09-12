import googleSearch
import aylien
import sys

phoneNo = sys.argv[1]

url_array = googleSearch.getGoogleLinks(phoneNo)

for url in url_array:
    aylien.getCategorySpecific(url)