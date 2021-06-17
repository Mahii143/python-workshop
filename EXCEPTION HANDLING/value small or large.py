class ValueTooSmallError(Exception):
    def display(self):
        print("You entered small value")
class ValueTooLargeError(Exception):
    def display(self):
        print("You entered large value")

maxVal = 100
while 1:
    try:
        num = int(input())
        if num == maxVal:
            print("You win")
            break
        if num < maxVal:
            raise ValueTooSmallError
        elif num > maxVal:
            raise ValueTooLargeError
    except ValueTooSmallError as e:
        e.display()
    except ValueTooLargeError as e:
        e.display()
