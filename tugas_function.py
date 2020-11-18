print('Penjumlahan Bilangan')

def total(deret:int):
    return sum(deret)

if __name__ == "__main__":
    deret = input('Bilangan\t:').split(" ")
    deret=list(map(int, deret))

    print(f'Jumlah Bilangan\t: {total(deret)}')