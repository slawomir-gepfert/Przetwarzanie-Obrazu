Przetwarzanie obrazu w Pythonie

Opis projektu

Program pobiera obraz z Wikimedia Commons na podstawie podanego adresu URL, a następnie wykonuje podstawowe operacje przetwarzania obrazu:

wyświetlenie obrazu oryginalnego,

zmniejszenie rozdzielczości o 50%,

konwersja do skali szarości (grayscale),

obrót obrazu o 90 stopni,

wyświetlenie obrazu wynikowego,

wyświetlenie macierzy pikseli obrazu.

Wymagane biblioteki

pip install opencv-python matplotlib

Uruchomienie programu
python main.py
Przykładowe działające adresy URL

https://upload.wikimedia.org/wikipedia/commons/6/63/Klematis.jpg

https://upload.wikimedia.org/wikipedia/commons/2/24/Konica_C35.jpg

https://upload.wikimedia.org/wikipedia/commons/5/5e/Lagonda_M45_Tourer%2C_Bj._1933_%282009-08-07%29_ret2_Sp.jpg

Uwagi
Adres obrazu powinien rozpoczynać się od:

https://upload.wikimedia.org

Niektóre adresy Wikimedia Commons mogą zwracać błąd HTTP 429. W takim przypadku należy spróbować użyć innego obrazu lub ponownie skopiować adres URL.
