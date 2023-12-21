import aiohttp
from aiohttp import web


async def long_polling_handler(request):
    async with aiohttp.ClientSession() as session:
        while True:
            data = await request.json()  # Parse JSON data from the request body
            return web.json_response({"name":data["name"]}) # Send received result back
        
# Register routes
app = web.Application()
app.router.add_get('/long_polling', long_polling_handler)

if __name__ == '__main__':
    web.run_app(app)
