import asyncio
import aiohttp
import aiofiles
import os
from urllib.parse import urlparse
from tempfile import TemporaryDirectory


async def download_chunk(session, url, headers, save_path):
    """Download a specific byte range of a file."""
    async with session.get(url, headers=headers) as response:
        content = await response.content.read()
        async with aiofiles.open(save_path, "wb") as f:
            await f.write(content)

async def get_file_size(session, url):
    """Get total file size using HEAD request."""
    async with session.head(url) as response:
        return int(response.headers.get("Content-Length", 0))


async def download_fast(url, dest_dir="./downloads"):
    """Download a file using multipart chunks for speed."""
    os.makedirs(dest_dir, exist_ok=True)
    filename = os.path.basename(urlparse(url).path)

    async with aiohttp.ClientSession() as session:
        total_size = await get_file_size(session, url)
        part_size = 10 * 1024 * 1024  # 10MB chunks

        with TemporaryDirectory() as tmp_dir:
            tasks = []
            for i in range(0, total_size, part_size):
                end = min(i + part_size - 1, total_size - 1)
                chunk_path = os.path.join(tmp_dir, f"part_{i}.bin")
                headers = {"Range": f"bytes={i}-{end}"}
                tasks.append(download_chunk(session, url, headers, chunk_path))

            await asyncio.gather(*tasks)

            # Concatenate parts
            final_path = os.path.join(dest_dir, filename)
            async with aiofiles.open(final_path, "wb") as f:
                for i in range(0, total_size, part_size):
                    part_path = os.path.join(tmp_dir, f"part_{i}.bin")
                    async with aiofiles.open(part_path, "rb") as pf:
                        await f.write(await pf.read())

            print(f"Downloaded {filename} to {final_path}")


# Usage
asyncio.run(
    download_fast(
        "https://video-downloads.googleusercontent.com/ADGPM2khQJ3jxhG3vxa-Cy7GW3cmPBUf36kqfGTKffTViwbV3oSRROQPvViviT-YZEQoXa10L6wa7VGX21g_S5nd8TI_Y6fA9VsumFeRakdZI_TUp6c_beiR-hPK1RBiv5oR7QacgogKBzmhMGKBX5QakyICeXEbF0fTaTGaORFvbu6vjm7WYL48tQwbPxELVYrr8x-DlDk8AwFbx0JvycMlgu2XmttPh16NOtlJJszwFD42YILZakEuUkrhkPtNE5k-2aK92nsTId0W_46VExJLlbUR1Xt64-L04ZngnSIUMTY5xde4aQmEfqB4hkfjl0hztusA_zVOAIQFjjvHOPCueI-7LL83tqYcnlvx0hM8RK_FBbyAWPcNpMklRTqfFb6V_KTO6j4HfNOpufKoVwSsFWhhZzN3HcuiInoRF1Xp0ZGf1aAEDSp5FPRo98OfgKQit2u2RjbLiQ9FPQcqjXZWn-kByHpdViUj3Qp4vKmGRYmuP3X8UK4WmlJU0GH02AJd6ZFzvyhFu_rzrcLdnzPsFv6rGl-MxHmVkaQIObBJ_JvZJK2wQecyMhqnDmB2qPJzLikKTf3s4uep4MGcOfZ74nlhNb69Rsff32V17B3n6kA68A_5vhO0X_Sr4AgSakJcKEUmuO2pOz9utZBADX6df72gdv5s_DdAi5APUUOPpk5v40AtA-MQ-w_heMFFTzfoMViemUBn07qL4xPpbmNfc4p13JHNLNgS4MJJctOK7rtU_u_HKqHiagU3AyTto0bMw34OYj8asP_j6N4ZFDI_XPEADyu0tFzIKMoEqPN5XD3hI4_8omTwwEFc9KaoJ7bpqovzlJNfThWzbXqZpMsaWucQNTdyxWCww4IB9yrTzwaT2lOvPqcVLNpHrix43bhhwOoGeWWh1voN6YY7zQ8YPgu8nwjA4eUIfUgZdxxtEUqajnQ4GndUOWKNrskndn_vsITQaX_4qSC_K_4YHlKSAhj1ZrLxIJEE2KbrF4ZWIXQ5iXNGSvH_u2GgaJo7gyBkqiRK-Gl4gLmGp8p4F7b_v9K7xSNSBa5LjO7KX4FOfV1KC01TVPNZA3TXnR3YgAnPVFBbVZOT"
    )
)
