// function solution(n) {
//     //먼저 0부터 n까지의 숫자가 소수인지 여부를 담은 배열 생성
//     //n = 0인 경우를 생각하여 count.length === n + 1
//     const count = Array(n+1).fill(true);
//     count[0] = count[1] = false;
//     //배열요소 i
//     for(let i = 2; i <= n; i++) {
//         //약수가 될 j
//         for(let j = 2; j <= parseInt(Math.sqrt(n)); j++) {
//             //j !== 나누는 수 && j로 나눠지는 경우
//             if(i !== j && i % j === 0) count[i] = false;      
//         }
//     }
//     return count.filter(v => v === true).length
// }

//위와 같이 푼 결과 효율성 테스트에서 실패해서 조건을 추가했다.

function solution(n) {
    //먼저 0부터 n까지의 숫자가 소수인지 여부를 담은 배열 생성
    //n = 0인 경우를 생각하여 count.length === n + 1
    const count = Array(n+1).fill(false);
    count[0] = count[1] = true;
    //배열요소 i
    for(let i = 2; i <= n; i++) {
        if(count[i] === false) {
            //나누는 조건은 소수로만 확인하면 된다
            for(let j = i * i; j <= n; j += i) {
                count[j] = true
            }
            }            
        }
    return count.filter(v => v === false).length
}