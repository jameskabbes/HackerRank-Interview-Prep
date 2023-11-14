function gradingStudents(grades){

    for (let i=0; i<grades.length; i++){
        grades[i] = grade( grades[i] )
    }
    return grades
}
    
function grade( score ){
    if (score < 38){
        return score
    }
    
    const mod = score % 5
    if (mod >= 3){
        return score + (5-mod)
    }
    
    return score

}

    
