import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

def download_image(image_url):
    print(f"Download the image {image_url}")
    image_filename = image_url.split("/")[-1].replace("?", "_").replace("=", "_").replace("&", "_")
    image_filename = "IMAGES" + "/" + image_filename
    response = requests.get(
        image_url, headers=HEADERS, verify=False, timeout=10
    )
    with open(image_filename, "wb") as f:
        for chunk in response.iter_content(2000):
            f.write(chunk)

if __name__ == "__main__":
    urls = [
        "https://lavedette.net/wp-content/uploads/2020/01/logo_vedette_200_60.png",
    ]

    for url in urls:
        download_image(url)
