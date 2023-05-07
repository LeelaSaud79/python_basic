import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title ="Relax!!",
            message = "You can do it, don't panic",
            timeout = 20
        )
        time.sleep(2400)


