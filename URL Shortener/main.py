from bitlyshortener import Shortener
access_token="****************************************"
long_url=input("Enter the URL to shorten: ")
short_url=Shortener(tokens=[access_token]).shorten_urls([long_url])[0]
print(f"Shortened URL: {short_url}")
