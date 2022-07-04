//최대공약수: 유클리드 공식
//큰 수 A를 작은 수 B로 나누어 떨어지면 최대공약수는 B
//A % B === R일 때 A,B의 최대공약수 === R,B의 최대공약수
//최소공배수: A * B / 최대공약수

const solution = (n, m) => {
    const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
    const lcm = (a, b) => a * b / gcd(a, b);
    return [gcd(n, m), lcm(n, m)];
}
