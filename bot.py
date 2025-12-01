import tgvip  # NOT ultra_neo_sender

# Inject BOT_TOKEN & API
tgvip.BOT_TOKEN = "8330501816:AAHsNLzOevZcSQZ6T1OyZ9TUjFf9B-Cq7gc"
tgvip.API = f"https://api.telegram.org/bot{tgvip.BOT_TOKEN}/sendMessage"

# Run the sender
tgvip.main()
