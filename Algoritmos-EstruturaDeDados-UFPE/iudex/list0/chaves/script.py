def main():
    lines = ''
    try:
        while True:
            lines = input()
    except:
        pass
    if len(lines) == 0 :
            print("S")
    else:
        if lines[-2] == "{" or lines[-1] == "{":
            print("N")
        elif lines.index("}") == 0:
            print("N")
        else:
            qtd1 = lines.count("{")
            qtd2 = lines.count("}")
            if qtd1 == qtd2:
                print("S")
            else:
                print("N")

if __name__ == '__main__':
    main()