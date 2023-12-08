import asyncio
import bleak
from bleak import BleakScanner
# from bleak import BleakClient


async def discover():
    devices = await BleakScanner.discover()
    return devices

async def connect(device_address):
    async with bleak.BleakClient(device_address) as client:
        print(f"Łączenie z {device_address}")

        await client.connect(timeout = 10)

        # if await client.is_connected():
        if (client.connect() == 1):
            print("Połączono")
            # Przykładowa charakterytyka, która może być dostępna do zapisu na urządzeniu BLE
            characteristic_uuid = "0000FFE1-0000-1000-8000-00805F9B34FB" #"0000ffe1-0000-1000-8000-00805f9b34fb"

            # Konwertuj dane na bajty (bytes) przed wysłaniem
            data_to_send = "Hello, BLE World!"
            data_bytes = data_to_send.encode('utf-8')

            # Wysyłanie danych do charakterystyki
            await client.write_gatt_char(characteristic_uuid, data_bytes)
            print("wysyłanie")
        await asyncio.sleep(5)  # Przykładowe oczekiwanie przez 5 sekund

        await client.disconnect()

async def main():
    device_name_to_find = "BT05"
    iDeviceIndex = -1

    devices = await discover()

    if devices:
        print("Znalezione urządzenia:")
        for index, device in enumerate(devices):
            print(f"{index}. Name: {device.name}, Address: {device.address}")
            if device.name == device_name_to_find:
                iDeviceIndex = index

        if iDeviceIndex >= 0:
            print(f"\nZnaleziono urządzenie o nazwie '{device_name_to_find}' na indeksie {iDeviceIndex}, z adresem {devices[iDeviceIndex].address}.")
            device_address = devices[iDeviceIndex].address
            await connect(device_address)
        else:
            print(f"\nNie znaleziono urządzenia o nazwie '{device_name_to_find}'.")

    else:
        print("Nie znaleziono żadnych urządzeń BLE.")


if __name__ == "__main__":

    asyncio.run(main())
    # asyncio.run(connect("D0:39:72:C3:1D:06"))
