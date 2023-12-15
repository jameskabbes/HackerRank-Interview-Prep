def mars_exploration(s)
    correct_message = 'SOS'
    changed_letters = 0
  
    s.chars.each_with_index do |char, index|
      if char != correct_message[index % correct_message.length]
        changed_letters += 1
      end
    end
  
    changed_letters
  end
  