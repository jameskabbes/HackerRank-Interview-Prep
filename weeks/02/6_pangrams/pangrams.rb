def pangrams(s)
    alphabet = ('a'..'z').to_set
    string_set = s.downcase.chars.to_set
  
    alphabet.each do |letter|
      unless string_set.include?(letter)
        return 'not pangram'
      end
    end
  
    'pangram'
  end
  