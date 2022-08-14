function solution(n) {
    let count = 1;
    if(n <= 1) return n;
    for(let i = 2; i <= n; i++) {
        if(n % i === 0) count += i;
    }
    return count;
}