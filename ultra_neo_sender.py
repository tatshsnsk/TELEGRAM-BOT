import ultra_neo_sender

# Inject BOT_TOKEN & API
ultra_neo_sender.BOT_TOKEN = "8330501816:AAHsNLzOevZcSQZ6T1OyZ9TUjFf9B-Cq7gc"
ultra_neo_sender.API = f"https://api.telegram.org/bot{ultra_neo_sender.BOT_TOKEN}/sendMessage"

# Run the sender
ultra_neo_sender.main()
