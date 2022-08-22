function solution(n) {
    let result = '';
    for(let i = 0; i < n; i++) {
        i % 2 === 0 ? result += '수' : result += '박';
    }
    return result;
}