
def main():
    free_space, users_q = [int(x) for x in input().split()]

    users_arr = []
    for i in range(users_q):
        users_arr.append(int(input()))
    archived_users = 0
    users_arr.sort()
    for need_space in users_arr:
        if need_space <= free_space:
            archived_users += 1
            free_space -= need_space
        else:
            break
    print(archived_users)


if __name__ == "__main__":
    main()
