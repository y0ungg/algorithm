function solution(s) {
    let middle = (s.length - 1) / 2;
    
    if (s.length % 2) return s[middle];
    else {
        return s.slice(middle - 0.5, middle + 1.5);
    };
}