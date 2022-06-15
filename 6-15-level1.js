//입력: 정수x, 자연수n
//출력: 배열
//요소는 x, x+x, x+x+x, ... n개

function solution(x, n) {
    var answer = [];
    const num = x;
    for(let i=1; i <=n; i++) {
        answer.push(x);
        x += num;
    }
    return answer;
}

//더 좋은 방법이 있을 것 같지만 일단은 이렇게...
