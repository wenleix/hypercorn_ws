# Start Hypercorn Server
```
pip install -r requirements.txt
hypercorn app:app
```

# Create WebSocket Connection to Server
```
python -m websockets ws://127.0.0.1:8000/test
```

# Results

Server side log shows error in ASGI framework due to uncaught exception:

```
[2023-05-24 10:56:06 -0700] [53929] [ERROR] Error in ASGI Framework
Traceback (most recent call last):
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/hypercorn/asyncio/task_group.py", line 23, in _handle
    await app(scope, receive, send, sync_spawn, call_soon)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/hypercorn/app_wrappers.py", line 33, in __call__
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/fastapi/applications.py", line 271, in __call__
    await super().__call__(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/applications.py", line 118, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/middleware/errors.py", line 149, in __call__
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
    raise exc
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
    await self.app(scope, receive, sender)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/routing.py", line 706, in __call__
    await route.handle(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/routing.py", line 341, in handle
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/starlette/routing.py", line 82, in app
    await func(session)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/hypercorn_ws/lib/python3.9/site-packages/fastapi/routing.py", line 289, in app
    await dependant.call(**values)
  File "/Users/wx/code/hypercorn_ws/app.py", line 8, in test
    raise RuntimeError("failed")
RuntimeError: failed
```

However, client side receives connection closed with 1000 (`CLOSE_NORMAL`):
```
Connected to ws://127.0.0.1:8000/test.
Connection closed: 1000 (OK).
```
