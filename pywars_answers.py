from __future__ import print_function
import pyWars
#import local_pyWars as pyWars

def answer1(datasample):
    return datasample+5

def main():
    print("#1", d.answer( 1, answer1(d.data(1))))


if __name__ == "__main__":
    d = pyWars.exercise()
    d.login("YourUsername","YourPassword")
    main()
    d.logout()
