function solution(a, b) {
    const left = Math.min(a, b);
    const right = Math.max(a, b);
    let middle = left + 1;
    let sum = left;
    
    if (a === b) return sum;
    
    while (middle <= right) {
        sum += middle;
        middle += 1;
    }
    return sum;
}