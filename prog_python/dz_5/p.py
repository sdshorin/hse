from collections import namedtuple


def main():
    SchoolResult = namedtuple("SchoolResult", ["activity", "school_num"])
    counted = [SchoolResult(0, x) for x in range(101)]
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            school = int(line.split()[2])
            counted[school] = SchoolResult(
                counted[school].activity + 1,
                counted[school].school_num)
    counted.sort(key=lambda school: school.school_num)
    counted.sort(key=lambda school: school.activity, reverse=True)
    top_activity = counted[0].activity
    print(" ".join([str(i.school_num)
                    for i in counted if i.activity == top_activity]))


if __name__ == "__main__":
    main()
