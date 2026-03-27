import datetime

def log(level, message):
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] {level.upper()}: {message}")

def info(message):
    log("info", message)

def error(message):
    log("error", message)
