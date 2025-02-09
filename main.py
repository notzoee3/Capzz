import asyncio
import websockets
import json

# Daftar Node ID yang akan diping
NODE_IDS = [
    "6IMIKXFGXQVP",
    "HB0MQMD9VPGD",
    "EA9Q2J6RH2SF",
    # Tambahkan lebih banyak Node ID jika tersedia
]

CAPFIZZ_WS_URL = "wss://capfizz.com/ws"  # Ganti dengan URL WebSocket yang benar

async with websockets.connect("wss://mainnet-realtime.capfizz.com/socket.io/?EIO=4&transport=websocket") as ws:
            ping_data = {
                "action": "ping",
                "node_id": node_id
            }
            await ws.send(json.dumps(ping_data))
            response = await ws.recv()
            print(f"Ping response for node {node_id}: {response}")
    except Exception as e:
        print(f"Error on node {node_id}: {e}")

async def main():
    tasks = [ping_node(node_id) for node_id in NODE_IDS]
    await asyncio.gather(*tasks)  # Menjalankan semua node bersamaan

if __name__ == "__main__":
    asyncio.run(main())
