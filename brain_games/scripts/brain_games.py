#!/usr/bin/env python3
from brain_games.cli import welcome_user


def greeting():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def main():
    greeting()


if __name__ == '__main__':
    greeting()
