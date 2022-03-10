import time





print("Pomodoro starts now!")
'''
Traditional technique to manage time in work and studies.
Timer starts with 25-minutes and 5-minutes intervals
Methods: 
    Loop to 
'''
for i in range(4):
    goTiktok = 25*60
    '''
    Convers 25 minutes to 1500 seconds
    '''
    while goTiktok:
        mins = goTiktok // 60
        '''
        floor division converting time into minutes
        '''
        secs = goTiktok % 60
        '''
        Modulous to from help find remainder in seconds
        '''
        timer = '{:02d}:{:02d}'.format(mins, secs)
        '''
        Format for size (2 width, 0 padding left) and d for a digit value
        '''
        print(timer, end='\r')
        '''
        Print timer and help avoid ovewriting timer
        '''
        time.sleep(1)
        '''
        Timer to sleep for a second before count down 
        '''
        goTiktok -=1
        '''
        Decrement timer by one second
        '''
print('Break Time!!')
'''
Five minutes break
'''
goTiktok = 5*60
'''
    Converts five minutes to seconds
'''
while goTiktok:
    '''
    Loop to execute countdown
    '''
    mins = goTiktok // 60
    '''
    floor division converting time into minutes
    '''
    secs = goTiktok % 60
    '''
        Modulous to from help find remainder in seconds
    '''
    timer = '{:02d}:{:02d}'.format(mins, secs)
    '''
        Format for size (2 width, 0 padding left) and d for a digit value
    '''
    print(timer, end='\r')
    '''
        Print timer and help avoid ovewriting timer
    '''
    time.sleep(1)
    '''
        Timer to sleep for a second before count down 
    '''
    goTiktok -=1
print('Work Time!')
        