def main():
    lines = []
    largest = ""
    length = -1
    try:
        while True:
            lines.append(input())
    except:
        pass
    for line in lines:
        if line != '[]':
            qtd = line.count(",") + 1
            if qtd > length:
                length = qtd
                largest = line
    
    print(largest)
        

if __name__ == '__main__':
    main()