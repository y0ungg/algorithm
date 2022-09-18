//약수 구하는 방법 --> N의 제곱근까지만 탐색한다
//그전에.. 여기서는 약수의 개수가 홀수인 경우를 판별하면 되므로
//약수의 개수가 홀수인 경우? --> N의 제곱근이 정수인 경우
function solution(left, right) {
    let result = 0;
    for (let i = left; i <= right; i++) {
        if(Math.sqrt(i) === Math.floor(Math.sqrt(i))) result -= i
        else result += i
    }
    return result;
}