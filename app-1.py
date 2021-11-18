# Pobieranie kolejnych wierszy z pliku tekstowego i konwersja do małej litery

# Kiedy przetwarzasz plik o bardzo dużej ilości wierszy, stosując
# list comprehension wszystkie pobrane dane musisz przechować w pamięci
print("------------------------------------------ 1 --------------------------------------------")
with open('data.txt') as data:
    lines = [line[:-1].lower() for line in data]
    print(lines)

# Możesz znacznie zoptymalizować ilość potrzebnej do zużycia pamięci
# poprzez zastosowanie generator expressions. Generator nie pobiera
# wszystkich danych, tylko dostarcza nam iterator, który pozwala
# pobierać dane po jednym elemencie, kiedy potrzebujemy go przetworzyć.
with open('data.txt') as data:
    it = (line[:-1].lower() for line in open('data.txt'))
    print(it)

    print("------------------------------------------ 2 --------------------------------------------")
    # Posiadając iterator pobierasz kolejne dane z pliku i ładujesz je do
    # pamięci dopiero wtedy, kiedy ich potrzebujesz
    print(it.__next__())
    print(next(it))

    # Generator expressions możesz łączyć w bardzo prosty sposób
    # W poniższym przykładzie na podstawie danych, które dostarcza iterator it
    # możemy zaimplementować kolejny generator
    print("------------------------------------------ 3 --------------------------------------------")
    it_2 = ((w, len(w)) for w in it)
    print(next(it_2))
    print(next(it_2))

# Wniosek:
# Generatory pozwalają optymalnie przetwarzać ogromne porcje danych.
# Wadą jest konieczność posługiwania się iteratorem, co nie musi być
# wygodne oraz przy nieodpowiednim stosowaniu może powodować błędy
# przy odczycie danych ( np. możesz pominąć niektóre dane )