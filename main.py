import requests

'''
  parameters: website: string that contains a website 
  
  return: return a string with the website encoding 
  
  dependences: module requests
'''
def getShortUrl(website):
    shortUrl=requests.get("http://tinyurl.com/api-create.php?url="+website);
    return shortUrl.content.decode("utf-8")



print("Ejemplo de como acortar un url")
website="https://www.google.com.mx/"
website="https://www.google.com/search?q=acortar+url+con+js&client=ubuntu&hs=fJY&channel=fs&sxsrf=APq-WBt0ZHJ7Y2RyIz8JJF1GpwO5r9hUOQ%3A1646169083462&ei=-4seYu7nG7mfkPIPz8OiiAE&ved=0ahUKEwiu0dbb6aX2AhW5D0QIHc-hCBEQ4dUDCA0&uact=5&oq=acortar+url+con+js&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECc6BwgjELADECc6BwgAEEcQsAM6BwgjEOoCECc6BggjECcQEzoECAAQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6BQgAEIAEOg4ILhCABBCxAxDHARCjAjoICAAQgAQQsQM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBOgcIABCxAxBDOg0IABCABBCHAhCxAxAUOgoIABCABBCHAhAUOgYIABAWEB5KBAhBGABKBAhGGABQ1AZYriZgsihoBHABeACAAakCiAH6GJIBBjAuMTUuM5gBAKABAbABCsgBCcABAQ&sclient=gws-wiz"
url=getShortUrl(website)
print("la url acortada es ",url)