import time
import client_mysql

from aiohttp import web

class MyView(web.View):
    async def post(self) -> web.StreamResponse:
        data = await self.request.post()
        client.insert(data)
        time.sleep(10)
        return web.json_response("Data added to database")


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




client = client_mysql.Client_MySQL('test', 'password')
web.run_app(init())
