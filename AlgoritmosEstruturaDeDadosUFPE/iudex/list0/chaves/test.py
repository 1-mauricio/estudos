def main():
    lines = input()
    teste = []
    
    for i in range(len(lines)):
        if lines[i] == "{":
            teste.append("{")
            
        elif lines[i] == "}":
            if len(teste) > 0:
                teste.pop()
            
            else:
                teste.append('}')
                
    
    if len(teste) == 0:
        print("S")
    else:
        print("N")


if __name__ == '__main__':
    main()