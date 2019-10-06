import requests as re
import pyperclip
import json
import sys

def get_api_key():
    with open("config.json", "r") as file:
        config = json.loads(file.read())
        return config["api_key"]

def get_file_data(file):
    with open(file, "r") as file:
        return file.read()

def paste(file):
    api_data = {
        "api_dev_key":get_api_key(),
        "api_option":"paste",
        "api_paste_code":get_file_data(file),
    }

    ext = file.split(".")[-1]
    with open("formats.json", "r") as file:
            fmt = json.loads(file.read())

            if ext in fmt:
                ext = fmt[ext]
            else:
                ext = "text"
    
    api_data["api_paste_format"] = ext

    r = re.post("https://pastebin.com/api/api_post.php", data=api_data)

    return r.text

if __name__ == "__main__":
    file = sys.argv[1]

    url = paste(file)
    pyperclip.copy(url)
    print("File pasted to:", url)