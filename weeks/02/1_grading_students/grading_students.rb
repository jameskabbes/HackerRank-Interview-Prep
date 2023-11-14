def gradingStudents(grades)
    grades.map! { |score| grade(score) }
    return grades
end


def grade(score)
    if score < 38
        return score
    end

    mod = score % 5
    if mod >= 3
        return score + (5 - mod)
    end

    return score
end
  
