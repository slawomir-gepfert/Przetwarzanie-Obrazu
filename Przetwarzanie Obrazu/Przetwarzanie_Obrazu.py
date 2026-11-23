# Wymagane biblioteki:
# pip install opencv-python matplotlib

import urllib.request
import cv2
import matplotlib.pyplot as plt


def pobierz_obraz(url):
    naglowki = {
        "User-Agent": "Mozilla/5.0"
    }

    print("\nPobieranie:")
    print(url)

    request = urllib.request.Request(url, headers=naglowki)

    with urllib.request.urlopen(request) as odpowiedz:
        dane = odpowiedz.read()

    with open("obraz.jpg", "wb") as plik:
        plik.write(dane)

    obraz = cv2.imread("obraz.jpg")

    return obraz


def wyswietl_obraz(obraz, tytul):
    plt.figure(figsize=(6, 6))

    if len(obraz.shape) == 2:
        plt.imshow(obraz, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(obraz, cv2.COLOR_BGR2RGB))

    plt.title(tytul)
    plt.axis("off")
    plt.show()


def przetworz_obraz(obraz):
    nowa_szerokosc = int(obraz.shape[1] * 0.5)
    nowa_wysokosc = int(obraz.shape[0] * 0.5)

    obraz = cv2.resize(obraz, (nowa_szerokosc, nowa_wysokosc))

    obraz = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)

    obraz = cv2.rotate(obraz, cv2.ROTATE_90_CLOCKWISE)

    return obraz


def wyswietl_macierz(obraz):
    print("\nMacierz obrazu:\n")
    print(obraz)


def pobierz_poprawny_obraz():
    print("Program pobiera obrazy z Wikimedia Commons.")
    print("Podaj bezposredni adres obrazu rozpoczynajacy sie od:")
    print("https://upload.wikimedia.org")
    print()

    print("Przykladowe sprawdzone adresy:")
    print("https://upload.wikimedia.org/wikipedia/commons/6/63/Klematis.jpg")
    print("https://upload.wikimedia.org/wikipedia/commons/2/24/Konica_C35.jpg")
    print("https://upload.wikimedia.org/wikipedia/commons/5/5e/Lagonda_M45_Tourer%2C_Bj._1933_%282009-08-07%29_ret2_Sp.jpg")
    print()

    print("Uwaga:")
    print("- Niektore adresy Wikimedia Commons moga zwracac blad 429.")
    print()

    print("Aby zakonczyc program wpisz: koniec")

    while True:
        url = input("\nPodaj URL obrazu: ")

        if url.lower() == "koniec":
            return None

        if not url.startswith("https://upload.wikimedia.org"):
            print("Blad: adres musi zaczynac sie od https://upload.wikimedia.org")
            continue

        try:
            obraz = pobierz_obraz(url)

            if obraz is None:
                print("Nie udalo sie wczytac obrazu.")
                continue

            wysokosc, szerokosc, kanaly = obraz.shape

            if szerokosc > 1024:
                print("\nUwaga: szerokosc obrazu przekracza zalecane 1024 px.")
                print("Program bedzie kontynuowal dzialanie.\n")

            return obraz

        except Exception as e:
            if "429" in str(e):
                print("\nBlad 429: Wikimedia Commons odrzucilo zapytanie.")
                print("Sprobuj wybrac inny obraz lub ponownie skopiowac adres URL.\n")
            else:
                print("\nWystapil blad:")
                print(e)


def main():
    obraz = pobierz_poprawny_obraz()

    if obraz is None:
        print("Program zakonczony.")
        return

    print("\nWyswietlanie obrazu oryginalnego.")
    print("Zamknij okno obrazu przyciskiem X, aby przejsc do kolejnego etapu.")

    wyswietl_obraz(obraz, "Obraz oryginalny")

    obraz_wynikowy = przetworz_obraz(obraz)

    print("\nPrzetwarzanie obrazu zakonczone.")
    print("Wyswietlany jest obraz po zmniejszeniu, konwersji do skali szarosci i obrocie.")
    print("Zamknij okno obrazu przyciskiem X, aby wyswietlic macierz pikseli.")

    wyswietl_obraz(obraz_wynikowy, "Obraz po przetworzeniu")

    wyswietl_macierz(obraz_wynikowy)


main()