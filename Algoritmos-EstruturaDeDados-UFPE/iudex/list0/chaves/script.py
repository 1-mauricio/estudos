def main():
    lines = input()
    qtd1 = lines.count("{")
    qtd2 = lines.count("}")
    if qtd1 == qtd2:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    main()