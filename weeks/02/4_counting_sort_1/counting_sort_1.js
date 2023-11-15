function countingSort(arr){

    let freq_array = Array(100).fill(0);
    for (const integer of arr){
        freq_array[ integer ] += 1;
    }
        
    return freq_array

}
    
    
