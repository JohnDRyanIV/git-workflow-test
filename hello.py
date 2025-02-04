def testOut():
    expected = "This program is for testing github workflows"
    isValid = False
    if expected == message():
        isValid =  True
    else:
        isValid = False

    if isValid:
        print("test success")
    else:
        print("test fail")

def main():
    testOut()

def message():
    return "This program is for testing github workflows"

if __name__ == "__main__":
    main()


