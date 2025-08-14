import requests
url = 'https://api.pdfblocks.com/v1/remove_password'

body = {
  'file' : open('yash_bank_statement - Copy.pdf', 'rb'),
  'password' : '2508@2646'
}

headers = { 'X-Api-Key' : 'bcc7c3b09e7fd7ab3c09d0a67f2a2b35' }

response = requests.post(url, files=body, headers=headers)

if response.status_code == 200:
  with open('unencrypted.pdf', 'wb') as output:
    for chunk in response.iter_content():
        output.write(chunk)
else:
    print('Error:', response.status_code, response.text)