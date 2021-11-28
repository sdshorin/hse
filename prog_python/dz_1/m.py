from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Time:
    hours: int
    minutes: int
    seconds: int

    def __sub__(self: Time, other: Time):
        return Time(
            self.hours - other.hours,
            self.minutes - other.minutes,
            self.seconds - other.seconds)

    def to_seconds(self: Time):
        return self.seconds + 60 * (self.minutes + 60 * self.hours)

    def __str__(self: Time):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


def main():
    a = Time(int(input()), int(input()), int(input()))
    b = Time(int(input()), int(input()), int(input()))
#	print(b-a)
    print((b - a).to_seconds())


if __name__ == "__main__":
    main()
