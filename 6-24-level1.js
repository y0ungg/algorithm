//입력: 양의정수 x
//하샤드 수 = x의 각 자릿수의 합으로 x가 나누어져야 한다
//출력: 하샤드 수인지 여부
function solution(x) {
    let str = x.toString()
    let sum = 0;
    for (let i of str) {
        sum += +i
    }
    return x % sum === 0
}
