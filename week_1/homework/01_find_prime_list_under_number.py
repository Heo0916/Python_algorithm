input = 20

def find_prime_list_under_number(number):
    array = []

    for i in range(2, number+1):  # n의 범위 2 ~ n
        # i를 2, 3, 5, 7, 11
        # 2 ~ n-1 중에서 소수인 친구들만
        # 주어진 자연수 N이 소수이기 위한 필요 충분 조건
        # N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠 지지 않는다.
        # 수가 수를 나누면 몫 발생, 몫과 나누는 수 둘중 하나는 반드시 N의 제곱근 이하.
        for j in array:   # i의 범위 2 ~ n-1
            if i % j == 0 and j * j <= i:
                break
        else:
            array.append(i)

        count = 0

    return array


result = find_prime_list_under_number(input)
print(result)