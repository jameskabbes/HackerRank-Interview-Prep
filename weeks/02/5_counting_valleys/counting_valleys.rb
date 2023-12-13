def countingValleys(steps, path)
    in_mountain = false
    in_valley = false
    mountains = 0
    valleys = 0
    elevation = 0
  
    path.each_char do |p|
      if p == 'D'
        if elevation == 0
          in_valley = true
        end
        elevation -= 1
      end
  
      if p == 'U'
        if elevation == 0
          in_mountain = true
        end
        elevation += 1
      end
  
      if elevation == 0
        if in_mountain
          mountains += 1
        end
        if in_valley
          valleys += 1
        end
        in_mountain = false
        in_valley = false
      end
    end
  
    valleys
  end
  