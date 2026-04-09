import asyncio
import httpx

urls = [
    "https://www.pexels.com/search/4k%20field/",
    "https://pixabay.com/photos/nature-waters-lake-island-3082832/",
    "https://www.vecteezy.com/free-photos/desktop-wallpaper-4k",
    "https://www.freepik.com/free-photos-vectors/4k-uhd-wallpapers",
]


# We use one generic function instead of four identical ones
async def download_file(client, url, index):
    print(f"Starting download: {url[:30]}...")
    try:
        response = await client.get(url, follow_redirects=True)
        filename = f"ASIO{index}.avif"  # Changed to .html as these are web pages, not direct image links

        with open(filename, "wb") as f:
            f.write(response.content)
        return f"Successfully saved {filename}"
    except Exception as e:
        return f"Failed to download {url}: {e}"


async def main():
    # 'httpx.AsyncClient' is much faster for multiple requests
    async with httpx.AsyncClient() as client:
        tasks = []
        for i, url in enumerate(urls):
            tasks.append(download_file(client, url, i))

        # This runs all downloads concurrently
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
