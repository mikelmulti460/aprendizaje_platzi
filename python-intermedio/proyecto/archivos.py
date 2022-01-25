import numbers


def read():
    numbers = []
    with open("./archivo.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["mikel","gabiel","miguel","ariana","mariana"]
    with open("./names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def main():
    read()
    write()

if __name__ == "__main__":
    main()