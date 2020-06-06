import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water now",
            message = "The National academies of sciences, Engineering and Medicine determined that an adequate daily fluid intake is: about 15.5 cups of fluids for men. about 11.5cups of fluids for women.",
            timeout = 2
        )
        time.sleep(6)