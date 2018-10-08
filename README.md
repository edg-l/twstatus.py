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

# Note: asyncio.run is only available on 3.7+
# https://docs.python.org/3/library/asyncio-task.html#id3
asyncio.run(main())
```
