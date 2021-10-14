
def main():
    m_1, m_2 = map(int, input().split())
    n_1, n_2 = map(int, input().split())
    for i in range(m_1, m_2 + 1):
        for j in range(n_1, n_2 + 1):
            print(f"{i} x {j} = {i*j}")
        if i != m_2:
            print()


if __name__ == "__main__":
    main()
