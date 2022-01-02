Humans, without the imperfections
----------------------------------
NoBot is a python module for simulating typing and mouse movements, for example, a regular typing script would type "Hello, World", but mine, can mistype, then correct itself.
With a built in web function, perfect for bots.
Might implement a captcha solver in the future

----------------------------------
Usage:
from NoBot import WebService, NoBot

web = WebService.web()
keys = NoBot()

keys.type("Hello, world!")
