import asyncio
from bleak import BleakClient

async def main():
    ble_address = "realme Buds T110"  # Replace with your device's address
    characteristic_uuid = "98:34:8C:CC:48:C4"  # Replace with the characteristic UUID

    async with BleakClient(ble_address) as client:
        data = await client.read_gatt_char(characteristic_uuid)
        print(data)

asyncio.run(main())
