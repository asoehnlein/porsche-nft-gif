import os
import requests
from PIL import Image

nftid = input("Please enter the NFTID: ")

if not os.path.exists('images'):
    os.makedirs('images')

images = []

for rotation in range(0, 351, 10):
    image_url = f"https:--nft-evolution.web3.pdg-apps.io/_next/image?url=https%3A%2F%2Fconfigurator.porsche-digital-nft.mhp-immersive.com/static/0xCcDF1373040D9Ca4B5BE1392d1945C1DaE4a862c/{nftid}/{rotation}.png&w=2048&q=100"
    response = requests.get(image_url)

    if response.status_code == 200:
        filename = f'images/image_{rotation}.png'
        with open(filename, 'wb') as f:
            f.write(response.content)

        images.append(Image.open(filename))
        
        print(f"Downloaded image for rotation {rotation}")
    else:
        print(f"Failed to download image for rotation {rotation}. HTTP response code: {response.status_code}")

if images:
    images[0].save(f'{nftid}.gif', save_all=True, append_images=images[1:], loop=0)
    print(f"GIF created as {nftid}.gif")
    images[0].save(f'{nftid}_slow.gif', save_all=True, append_images=images[1:], loop=0, duration=200)
    print(f"Slow GIF created as {nftid}_slow.gif")
else:
    print("Failed to create GIF as no images were downloaded successfully.")