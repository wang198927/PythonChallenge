

import zipfile
import re

if __name__ == '__main__':

    z = zipfile.ZipFile('channel.zip', mode='r')

    preFix = '90052'
    surFix = '.txt'

    findNothing = re.compile('(\d+)')

    comments = []

    while True:

        text = z.read(preFix + surFix).decode()
        print(text)

        match = findNothing.search(text)

        if match:
            preFix = match.group(1)
            comments.append(z.getinfo(preFix + surFix).comment.decode())
        else:
            break

    print(''.join(comments))
