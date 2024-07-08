import requests

url = "https://www.ailabapi.com/api/portrait/effects/emotion-editor"

payload={'service_choice' : '3'}
files=[
  ('image_target',('file',open('closed-eyes-face-recognition-qdepjdihdmz3i8vxmpnmdhxf1c60iw2xu58ri17kqg.jpg','rb'),'application/octet-stream'))
]
headers = {
  'ailabapi-api-key': 'your-api-key-here'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# Save the entire response to a file
with open('response.txt', 'w') as file:
    file.write(response.text)

print("Response saved to response.txt")