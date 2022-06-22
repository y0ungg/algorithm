//입력: 전화번호 문자열
//뒷 4자리를 제외하고 *으로 변환한다.
//출력: 가려진 문자열

function solution(phone_number) {
    return '*'.repeat(phone_number.length - 4) + phone_number.slice(-4);
}
