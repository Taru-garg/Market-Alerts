# The alrt file

alrt file is just a simple way to store an alert. The file contains the following:
    -   Email (to which message will be sent on a sucessfull trigger)
    -   Market (BTC, ETH, DOGE)
    -   Condition/Reason for Trigger (price went above or below)
    -   Price 
    -   Time before next repitition ((seconds, multiple of seconds), (minutes, multiple of minutes), (Day, multiple of day))
    -   Last sucessfull execution   (will only be added by program internally and not entered by the user)
The same are the parameters of the alert class. Currently, although there is no support for the last two parameters and the trigger if
sucessfull will send a mail no matter what other things are specified, though it will be added soon enough. The GUI also currently has no way to add time before next repitition and can only be added by directly changing the alrt file. But anyways since it is not currently considered in any kind of processing or reporting, it is not useful. Once the support is added the app will be much more useful and functional.
