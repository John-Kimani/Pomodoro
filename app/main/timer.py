import time


tiktok = int(input('How many seconds do you want to set the timer?'))
'''
Variable to fetch time user set
'''

while tiktok:
    '''
    Loop that decreases time to zero seconds
    '''
    minutes = tiktok//60
    '''
    for division converting time into minutes
    '''
    seconds = tiktok % 60
    '''
    Modulous to from help find remainder
    '''
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    '''
    Format for size (2 width, 0 padding left) and d for a digit value'''
    print(timer, end='\r')
    '''
    Print timer and help avoid ovewriting timer
    '''
    time.sleep(1)
    '''
    Timer to sleep for a second before count down 
    '''
    tiktok -=1
    '''
    Decrement timer by one second
    '''
print('Time is up!')

