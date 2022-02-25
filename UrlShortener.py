import pyshorteners

banner = """
 dP     dP  888888ba  dP           .d88888b  dP                           dP                                       
88     88  88    `8b 88           88.    "' 88                           88                                       
88     88 a88aaaa8P' 88           `Y88888b. 88d888b. .d8888b. 88d888b. d8888P .d8888b. 88d888b. .d8888b. 88d888b. 
88     88  88   `8b. 88                 `8b 88'  `88 88'  `88 88'  `88   88   88ooood8 88'  `88 88ooood8 88'  `88 
Y8.   .8P  88     88 88           d8'   .8P 88    88 88.  .88 88         88   88.  ... 88    88 88.  ... 88       
`Y88888P'  dP     dP 88888888P     Y88888P  dP    dP `88888P' dP         dP   `88888P' dP    dP `88888P' dP       
                                                                                                                
                                                                          
     [!] URL Short
     [!] By : 4NDR0 R4T
     [!] www.hidayatcode.com
"""
print(banner)

long_url = input("Enter the URL to shorten: ")
 
#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)