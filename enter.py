import functools
import json
import time

from aiohttp import web

class MyView(web.View):
    async def get(self) -> web.StreamResponse:
        return web.json_response(
            {
                "method": self.request.method,
                "args": dict(self.request.rel_url.query),
                "headers": dict(self.request.headers),
            },
            dumps=functools.partial(json.dumps, indent=4),
        )

    async def post(self) -> web.StreamResponse:
        data = await self.request.post()
        time.sleep(10)
        return web.json_response("Ok")


async def index(request: web.Request) -> web.StreamResponse:
    txt = """
    <html>
        <head>
          <title>Class based view example</title>
        </head>
        <body>
          <h1>Class based view example</h1>         
        <form action="/send" method="post" accept-charset="utf-8"
      	    enctype="application/x-www-form-urlencoded">
    	    <label for="name">Name</label>
    	    <input id="name" name="name" type="text" value="" autofocus/>
    	    <p><label for="age">Age</label>
    	    <input id="age" name="age" type="age" value=""/></p>
	        <p><label for="city">City</label>
    	    <input id="city" name="city" type="city" value=""/></p>
	        <input type="submit" value="send"/>
        </form>
        </body>
    </html>
    """
    return web.Response(text=txt, content_type="text/html")

def init() -> web.Application:
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_post("/send", MyView)
    return app

web.run_app(init())
