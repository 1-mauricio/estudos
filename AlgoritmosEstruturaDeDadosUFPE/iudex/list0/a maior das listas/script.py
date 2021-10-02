import sys
def main():
    largest = ""
    length = -1
    for line in sys.stdin:
        line = line[:-1]
        qtd = line.count(',')
        if line != '[]':
            qtd += 1
        if qtd > length:
            length = qtd
            largest = line
    
    print(largest)
        

if __name__ == '__main__':
    main()