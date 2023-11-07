function miniMaxSum(arr) {
    let total = arr[0];
    let lowest_value = arr[0];
    let highest_value = arr[0];
    
    for (let i = 1; i < arr.length; i++) {
        total += arr[i];
        
        if (arr[i] < lowest_value) {
            lowest_value = arr[i];
        }
        if (arr[i] > highest_value) {
            highest_value = arr[i];
        }
    }
    
    let max_sum = total - lowest_value;
    let min_sum = total - highest_value;
    console.log(`${min_sum} ${max_sum}`);
}
