import tgvip  # NOT ultra_neo_sender

# Inject BOT_TOKEN & API
tgvip.BOT_TOKEN = "8322105794:AAF08sT_OnwjmaB8xMFhdGnf1YF9iLu7Gl8"
tgvip.API = f"https://api.telegram.org/bot{tgvip.BOT_TOKEN}/sendMessage"

# Run the sender
tgvip.main()
