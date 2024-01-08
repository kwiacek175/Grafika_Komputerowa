# Grafika Komputerowa
# Miniprojekt - Piramida Sierpińskiego 

# Opis projektu 
Ten projekt skupia się na implementacji piramidy Sierpińskiego przy użyciu języka Python i popularnych bibliotek do grafiki komputerowej - pygame oraz OpenGL.

# Narzędzia
Projekt został napisany w języku Python przy użyciu dwóch głównych bibliotek:

- Pygame: Biblioteka do tworzenia gier i aplikacji graficznych, idealna do prostych projektów graficznych.
- OpenGL: Otwarte środowisko graficzne, które umożliwia renderowanie trójwymiarowych scen.

# Instrukcje Uruchomienia
- Zainstaluj wymagane biblioteki, wykonując poniższą komendę:
```
pip install pygame PyOpenGL
```
- Pobierz projekt z tego repozytorium.
- Uruchom program za pomocą terminala lub w dowolnym środowisku programistycznym, które obsługuje Python.
``` 
python main.py
```

# Struktura Projektu
- main.py: Plik główny, który pełni rolę inicjatora programu. Odpowiada za stworzenie kontekstu graficznego, inicjalizację obiektów i zarządzanie główną pętlą programu.
- pyramid.py: Moduł zawierający implementację podstawowej piramidy. W tym pliku znajduje się klasa Pyramid, która posiada logikę rysowania piramidy w trójwymiarowej przestrzeni przy użyciu bibliotek OpenGL.
- sierpinskiPyramid.py: Moduł zawierający implementację algorytmu piramidy Sierpińskiego. Klasa SierpinskiPyramid generuje strukturę piramid Sierpińskiego na różnych poziomach rekurencji.

