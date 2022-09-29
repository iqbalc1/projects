### drinking water notification after 1 hour
 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
        title = "Time to Drink Water!", 
        message = "Dear Hana, Please go and Take one Glass of water. Love you!",
        app_icon = "C:\\Users\iqbalc\Desktop\Python Projects\Water Intake Reminder\icon.ico", timeout=10)
    time.sleep(6)

    ##time.sleep(60*60)