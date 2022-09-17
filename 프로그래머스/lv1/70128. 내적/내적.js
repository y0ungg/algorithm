function solution(a, b) {
    let len = a.length - 1;
    let result = 0;
    
    if(len < 0 || a.length === 0) return result;
    
    while(len >= 0) {
        result += (a[len] * b[len]);
        len--;
    }
    return result;
}