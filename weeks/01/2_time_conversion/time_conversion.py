def timeConversion(s):

    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    ampm = s[8:10]

    # edge cases
    if hour == '12' and ampm == 'AM':
        hour = '00'
    elif hour == '12' and ampm == 'PM':
        pass
    
    # generally
    else:
        if ampm == 'PM':
            hour = str( int(hour)+12 )            
        
    return '{}:{}:{}'.format(hour,minute,second)