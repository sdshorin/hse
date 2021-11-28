
def main():
    city_dict = {}
    country_q = int(input())
    for i in range(country_q):
        country, *cities = input().split()
        for city in cities:
            city_dict[city] = country
    question_q = int(input())
    for _ in range(question_q):
        city = input()
        print(city_dict[city])


if __name__ == "__main__":
    main()
