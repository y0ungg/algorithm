//n이 양의 정수의 제곱이면 (제곱근+1)의 제곱 리턴
//아닐시 -1 리턴
function solution(n) {
    const sqrt = Math.sqrt(n);
    if (sqrt % 1 === 0) return Math.pow(sqrt+1, 2); //정수는 1로 나누어 떨어진다
    return -1;
}
