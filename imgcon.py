import base64

# Load the response from the file
with open('response.txt', 'r') as file:
    response = file.read()

# Extract the Base64 string from the JSON response
import json
data = json.loads(response)
image_base64 = data['data']['image']

# Decode the Base64 string to binary data
image_data = base64.b64decode(image_base64)

# Save the binary data as an image file
with open('edited_image.jpg', 'wb') as image_file:
    image_file.write(image_data)

print("Image has been saved as 'edited_image.jpg'")
