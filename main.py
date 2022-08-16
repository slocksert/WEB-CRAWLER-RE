import requests
import re


url = input('Type the url:\n')
check = []
r = requests.get(url)
if r.status_code == 200:
    html = r.text.encode('utf8')
    search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode('utf8'))
    for link in search:
        if link not in check:
            check.append(link)
            with open('links.txt', 'a') as file:
                file.write(f'{link}\n')
else:
    print(f'Hey an error {r.status_code} just ocurred')
