# bot.py
TOKEN = "8330501816:AAHsNLzOevZcSQZ6T1OyZ9TUjFf9B-Cq7gc"

open("token.txt", "w").write(TOKEN)

import tgvip   # your .so module name
tgvip.main()
