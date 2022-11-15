import requests
import sys

print(API_KEY_ASSEMBLYAI)

# upload 
upload_endpoint = "https://api.assemblyai.com/v2/upload"
filename = sys.argv[1]

#filename = input("enter audio file")
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))

print(response.json())




# transcribe 

# poll

# save transcript

