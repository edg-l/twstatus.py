# twstatus.py
> Get the server information of teeworlds servers.

Tested on vanilla and ddnet based servers.

`pip install twstatus.py`

```python
from twstatus import ServerHandler
import asyncio

server = ServerHandler("1.1.1.1", 8303)

async def main():
    print(vars(await server.get_info()))

asyncio.run(main())
```
