def timeConversion(s)
    hour = s[0...2]
    minute = s[3...5]
    second = s[6...8]
    ampm = s[8...10]
  
    # edge cases
    if hour == '12' && ampm == 'AM'
      hour = '00'
    elsif hour == '12' && ampm == 'PM'
      # do nothing
    else
      if ampm == 'PM'
        hour = (hour.to_i + 12).to_s
      end
    end
  
    return "#{hour}:#{minute}:#{second}"
end