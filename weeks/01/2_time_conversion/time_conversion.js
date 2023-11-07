function timeConversion(s) {
    let hour = s.slice(0, 2);
    let minute = s.slice(3, 5);
    let second = s.slice(6, 8);
    let ampm = s.slice(8, 10);

    // edge cases
    if (hour === '12' && ampm === 'AM') {
        hour = '00';
    } else if (hour === '12' && ampm === 'PM') {
        // do nothing
    } else {
        if (ampm === 'PM') {
            hour = String(parseInt(hour, 10) + 12);
        }
    }

    return `${hour}:${minute}:${second}`;
}