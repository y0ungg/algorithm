//입력: 원래 이용료: price, 있는 돈: money, 몇 번째 횟수인지: count
//totalPrice = totalPrice + (price * i) --> count번까지 반복
//출력: totalPrice - money, 0보다 작으면 0을 리턴한다.
function solution(price, money, count) {
    let totalPrice = 0;
    for(let i = 1; i <= count; i++) {
        totalPrice = totalPrice + (price * i);
    }
    let result = totalPrice - money;
    console.log(totalPrice, money, result)
    return result >= 0 ? result : 0;
}