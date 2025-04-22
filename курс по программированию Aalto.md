# Template for C

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "myprint.h"

int main(void)
{
    ...
    return 0;
}
```

# .vimrc

```.vimrc
" Основные настройки Vim для экзамена
set nocompatible    " Отключение совместимости с Vi
syntax enable       " Подсветка синтаксиса
set number          " Номера строк
set tabstop=4       " 1 таб = 4 пробела
set shiftwidth=4    " Размер автоотступа = 4 пробела
set expandtab       " Преобразование табов в пробелы
set autoindent      " Автоотступы
set smartindent     " Умные отступы
set nowrap          " Отключить перенос строк
```

---

# Типы данных в си

В языке программирования **C** существуют следующие основные типы данных:

### 1. **Целочисленные типы** (хранят целые числа)

- `char` – символьный тип (1 байт, `-128` до `127` или `0` до `255`).

- `signed char` – знаковый символ (`-128` до `127`).

- `unsigned char` – беззнаковый символ (`0` до `255`).

- `short` (`short int`) – короткое целое (обычно 2 байта, `-32 768` до `32 767`).

- `unsigned short` (`unsigned short int`) – беззнаковый `short` (`0` до `65 535`).

- `int` – целое число (обычно 4 байта, `-2 147 483 648` до `2 147 483 647`).

- `unsigned int` – беззнаковый `int` (`0` до `4 294 967 295`).

- `long` (`long int`) – длинное целое (обычно 4 или 8 байт).

- `unsigned long` (`unsigned long int`) – беззнаковый `long`.

- `long long` (`long long int`) – очень длинное целое (обычно 8 байт).

- `unsigned long long` (`unsigned long long int`) – беззнаковый `long long`.

### 2. **Числа с плавающей запятой** (дробные числа)

- `float` – число с плавающей точкой (обычно 4 байта, ~7 знаков после запятой).

- `double` – двойная точность (обычно 8 байт, ~15 знаков после запятой).

- `long double` – расширенная точность (размер зависит от системы).

---

# Форматные спецификаторы в си

В языке **C** для вывода значений разных типов данных с помощью функции `printf()` используются специальные **форматные спецификаторы**. Вот основные из них:

### **1. Целочисленные типы**

| Тип данных            | Спецификатор `printf` | Пример использования            |
| --------------------- | --------------------- | ------------------------------- |
| `char`                | `%c`                  | `printf("%c", 'A');`            |
| `signed char`         | `%hhd` или `%c`       | `printf("%hhd", (char)-5);`     |
| `unsigned char`       | `%hhu` или `%c`       | `printf("%hhu", (uchar)200);`   |
| `short` (`short int`) | `%hd`                 | `printf("%hd", (short)-100);`   |
| `unsigned short`      | `%hu`                 | `printf("%hu", (ushort)500);`   |
| `int`                 | `%d`                  | `printf("%d", 42);`             |
| `unsigned int`        | `%u`                  | `printf("%u", 1000u);`          |
| `long` (`long int`)   | `%ld`                 | `printf("%ld", 123456L);`       |
| `unsigned long`       | `%lu`                 | `printf("%lu", 999999UL);`      |
| `long long`           | `%lld`                | `printf("%lld", 123456789LL);`  |
| `unsigned long long`  | `%llu`                | `printf("%llu", 123456789ULL);` |

### **2. Числа с плавающей запятой**

| Тип данных    | Спецификатор `printf`            | Пример использования            |
| ------------- | -------------------------------- | ------------------------------- |
| `float`       | `%f` или `%e` (экспоненциальная) | `printf("%f", 3.14f);`          |
| `double`      | `%lf` или `%e`                   | `printf("%lf", 2.71828);`       |
| `long double` | `%Lf`                            | `printf("%Lf", 3.1415926535L);` |

### **3. Указатели и специальные типы**

| Тип данных                        | Спецификатор `printf` | Пример использования          |
| --------------------------------- | --------------------- | ----------------------------- |
| Указатель (`void*`, `int*` и др.) | `%p`                  | `printf("%p", &x);`           |
| Строка (`char[]`, `char*`)        | `%s`                  | `printf("%s", "Hello");`      |
| Размер типа (`size_t`)            | `%zu`                 | `printf("%zu", sizeof(int));` |
| `ssize_t` (знаковый размер)       | `%zd`                 | `printf("%zd", -1);`          |

### **4. Дополнительные модификаторы**

- `%x` / `%X` – вывод в **шестнадцатеричном** формате (`unsigned int`).

- `%o` – вывод в **восьмеричном** формате (`unsigned int`).

- `%#x` / `%#o` – вывод с префиксом (`0x` для hex, `0` для octal).

- `%.2f` – вывод `float`/`double` с **2 знаками после запятой**.

- `%10d` – вывод числа в поле **шириной 10 символов** (выравнивание).

- `%-10d` – выравнивание **по левому краю**.

---

# switch

```
switch(a)
{
    case 1: // a == 1
      // statements to handle a is 1
      break;
    case 2: // a == 2
      // statements to handle a is 2
      break;
    case 3: // a == 3
      // statements to handle a is 3
      break;
    default: // (a != 1) && (a != 2) && (a != 3))
      // statements to handle unexpected value of a
      break;
}
```

---

# Макросы

```C
#define PI 3.14159
#define GREETING "Hello, World!"
```

```C
#define SQUARE(x) ((x) * (x))  // Квадрат числа
#define MAX(a, b) ((a) > (b) ? (a) : (b))  // Максимум из двух чисел
```

```C
#include <stdio.h>

int main() {
    printf("File: %s\n", __FILE__);  // Имя файла
    printf("Line: %d\n", __LINE__);  // Текущая строка
    printf("Date: %s\n", __DATE__);  // Дата компиляции
    printf("Time: %s\n", __TIME__);  // Время компиляции
    return 0;
}
```

---

# Динамическое выделение памяти

## 1. Выделение памяти

```C
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *arr1 = (int*)malloc(10 * sizeof(int)); // массив из 10 int
    double *arr2 = (double*)calloc(15, sizeof(double)); // массив из 15 double, инициализированных 0.0
    return 0;
}
```

## 2. Переназначение памяти

```C
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *arr = (int*)malloc(10 * sizeof(int)); // массив из 10 int
    arr = (int*)realloc(arr, 20 * sizeof(int)); // увеличиваем массив до 20 элементов
    return 0;
}
```

## 3. Освобождение памяти

```C
free(arr);
arr = NULL; // хорошая практика - обнулять указатель после освобождения
```

## 4. Valgrind

- скомпелировать файл main.out:  
  
  ```
  gcc -o main.out main.c
  ```

- Valgrind:  
  
  ```
  valgrind --leak-check=full --track-origins=yes --show-leak-kinds=all ./main.out
  ```

---

# Custom data types

## 1. enum

```C
#include <stdio.h>

enum Weekday {
    MONDAY,    // 0
    TUESDAY,   // 1
    WEDNESDAY, // 2
    THURSDAY,  // 3
    FRIDAY,    // 4
    SATURDAY = 5,  // 5
    SUNDAY = 6,     // 6
};

int main() {
    enum Weekday today = WEDNESDAY;
    if (today == WEDNESDAY) {
        printf("Сегодня среда!\n");
    }
    printf("Номер дня: %d\n", today); // Выведет: 2
    return 0;
}
```

## 2. struct

```C
#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
} Person;

struct Point {
    int x;
    int y;
};

int main() {
    Person Alex;
    strcpy(Alex.name, "Alexander");
    Alex.age = 18;

    Person *a = &Alex;
    printf("name: %s, \t age: %d\n", a->name, a->age);

    Person people[3] = {
        {"Алексей", 25},
        {"Мария", 30},
        {"Иван", 20}
    };

    struct Point p1;
    p1.x = 10;
    p1.y = 10;

    struct Point p2 = {.y = 25, .x = 30};

    return 0;
}
```

---

## 3. Битовые поля

Битовые поля — это специальная возможность структур в языке C, которая позволяет точно указывать, сколько бит должно использоваться для хранения каждого поля структуры.

```C
#include <stdio.h>

// Структура с битовыми полями
struct StatusRegister {
    unsigned int ready : 1;     // 1 бит (0 или 1)
    unsigned int error : 1;     // 1 бит
    unsigned int mode : 2;      // 2 бита (0-3)
    unsigned int value : 4;     // 4 бита (0-15)
};

int main() {
    struct StatusRegister status;

    status.ready = 1;
    status.error = 0;
    status.mode = 2;
    status.value = 9;

    printf("Размер структуры: %zu байт\n", sizeof(status));
    printf("ready: %u, error: %u, mode: %u, value: %u\n", 
           status.ready, status.error, status.mode, status.value);

    return 0;
}
```

---

# string.h [link](https://plus.cs.aalto.fi/elec-a7100/elect-a7100-spring-2025/M9-Stdlib-Basic-Functions/s2-strings/#:~:text=array%20manipulation%20functions-,class,-header)

## `strcpy`

```C
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello";
    char dest[10] = "12";
    strcpy(dest, src); // dest теперь содержит "Hello"
    printf("%s\n", dest); //Hello
    return 0;
}
```

## `strncpy`

```C
char src[] = "Hello";
char dest[10];
strncpy(dest, src, 3); // dest содержит "Hel\0"
```

## `strcat`

```C
char str[20] = "Hello";
strcat(str, " World"); // str теперь содержит "Hello World"
```

## `strncat`

```C
char str[20] = "Hello";
strncat(str, " World!", 3); // str теперь содержит "Hello Wo"
```

## `strcmp`

```C
#include <stdio.h>
#include <string.h>

int main() {
    int result1 = strcmp("apple", "banana");
    int result2 = strcmp("apple", "apple");
    int result3 = strcmp("apple", "appleapple");

    printf("%d, %d, %d\n", result1, result2, result3); //-1, 0, -1
    return 0;
}
```

## `strncmp`

```C
int result = strncmp("apple", "application", 3); // результат 0 (первые 3 символа совпадают)
```

## `strchr`

Находит первое вхождение символа `c` в строке `str`. Возвращает указатель на найденный символ или `NULL`.

```C
char *p = strchr("Hello", 'l'); // указывает на первую 'l'
```

## `strrchr`

```C
char *p = strrchr("Hello", 'l'); // указывает на вторую 'l'
```

## `strstr`

```C
char *p = strstr("Hello World", "World"); // указывает на начало "World"
```

## `strlen`

```C
size_t len = strlen("Hello"); // len = 5
```

## `strtok`

```C
char str[] = "one,two,three";
char *token = strtok(str, ",");
while (token != NULL) {
    printf("%s\n", token);
    token = strtok(NULL, ",");
}
//one
//two
//three
```

---

# time.h

```C
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>

int number_of_primes_less_than (int n) {
  int i, j;
  int count = n-1;
  for (i=2; i<=n; ++i) {
      for (j=sqrt(i); j>1; --j) {
          if (i%j==0) {
              --count;
              break;
          }
      }
  }
  return count;
}

int main(){
    struct tm* t;
    time_t seconds;
    clock_t ticks;
    int count;

    // get the time in seconds since epoch in UTC
    seconds = time(NULL);
    printf("The number of seconds since epoch %ld\n", seconds);
    // convert the seconds to time object of GMT time
    t = gmtime(&seconds);
    printf("Corresponding GMT time %02d:%02d:%02d %02d/%02d/%04d\n\n",
            t->tm_hour, t->tm_min, t->tm_sec,
            t->tm_mday, t->tm_mon, t->tm_year);
    // convert the seconds to time object of local time in local timezone
    t = localtime(&seconds);
    printf("Corresponding local time %02d:%02d:%02d %02d/%02d/%04d\n\n",
            t->tm_hour, t->tm_min, t->tm_sec,
            t->tm_mday, t->tm_mon, t->tm_year);
    // profile the number of seconds to calculate the
    // number of primes
    ticks = clock();
    printf ("Calculating...\n");
    count = number_of_primes_less_than(99999);
    printf ("The number of primes lower than 100,000 is: %d\n", count);
    ticks = clock() - ticks;
    printf ("Calculation took %ld ticks (%f seconds).\n",
            ticks, ((float)ticks)/CLOCKS_PER_SEC);
    return 0;
}
```

---

## Основные функции для генерации случайных чисел (stdlib.h)

### 1. **`int rand(void)`**

Генерирует псевдослучайное число в диапазоне от **`0`** до **`RAND_MAX`** (обычно `32767`).

```C
#include <stdio.h>
#include <stdlib.h>

int main() {
    int random_num = rand();
    printf("Случайное число: %d\n", random_num);
    return 0;
}
```

**Проблема**: При каждом запуске программы `rand()` выдаёт одну и ту же последовательность чисел.

### 2. **`void srand(unsigned int seed)`**

Устанавливает **начальное значение** (seed) для генератора случайных чисел.

- Если `seed` фиксирован (например, `srand(123)`), последовательность будет одинаковой.

- Для получения разных чисел при каждом запуске используют текущее время (`time(NULL)`).

```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h> // для time()

int main() {
    srand(time(NULL)); // Инициализация генератора
    int random_num = rand();
    printf("Случайное число: %d\n", random_num);
    return 0;
}
```

# Как получить случайное число в заданном диапазоне?

Функция `rand()` возвращает число от `0` до `RAND_MAX`, но часто нужно ограничить диапазон.

## Формула:

```C
// Случайное число в диапазоне [min, max]
int num = min + rand() % (max - min + 1);
```

## Пример:

```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));

    int min = 10, max = 20;
    int random_num = min + rand() % (max - min + 1);

    printf("Случайное число от %d до %d: %d\n", min, max, random_num);
    return 0;
}
```

---

# `qsort()`

```C
#include <stdio.h>
#include <stdlib.h>

// Функция сравнения для qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {5, 2, 8, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    qsort(arr, n, sizeof(int), compare);

    printf("Отсортированный массив:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

---

# `bsearch`

```C
#include <stdio.h>
#include <stdlib.h>

// Функция сравнения для сортировки и поиска
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {10, 20, 30, 40, 50}; // Отсортированный массив!
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 30; // Искомый элемент

    // Вызов bsearch
    int *result = (int*)bsearch(&key, arr, n, sizeof(int), compare);

    if (result != NULL) {
        printf("Элемент %d найден на позиции %ld\n", key, result - arr);
    } else {
        printf("Элемент %d не найден\n", key);
    }

    return 0;
}
```

---
# Работа с файлами
## Чтение файла
```C
FILE *file = fopen("input.txt", "r");
if (file == NULL) {
    perror("Ошибка открытия файла");
    return 1;
}

char buffer[100];

// Чтение строки (максимум 99 символов)
if (fgets(buffer, sizeof(buffer), file) != NULL) {
    printf("Прочитано: %s", buffer);
}

// Чтение символа
int ch = fgetc(file);
printf("Символ: %c\n", (char)ch);

// Форматированное чтение (например, числа)
int num;
fscanf(file, "%d", &num);
printf("Число: %d\n", num);

fclose(file);
```

## Запись в файл
```C
FILE *file = fopen("output.txt", "w");
if (file == NULL) {
    perror("Ошибка открытия файла");
    return 1;
}

fprintf(file, "Hello, World!\n");  // Форматированная запись
fputs("This is a line.\n", file);  // Запись строки
fputc('A', file);                  // Запись символа

fclose(file);
```
## Запись в бинарный файл
```C
#include <stdio.h>

int main() {
    FILE *file = fopen("data.bin", "wb");  // "wb" — бинарный режим записи
    if (!file) {
        perror("Ошибка открытия файла");
        return 1;
    }

    int numbers[] = {10, 20, 30, 40, 50};
    size_t elements_written = fwrite(numbers, sizeof(int), 5, file);

    if (elements_written != 5) {
        perror("Ошибка записи");
    }

    fclose(file);
    return 0;
}
```
## Чтение из бинарного файла
```C
#include <stdio.h>

int main() {
    FILE *file = fopen("data.bin", "rb");  // "rb" — бинарный режим чтения
    if (!file) {
        perror("Ошибка открытия файла");
        return 1;
    }

    int numbers[5];
    size_t elements_read = fread(numbers, sizeof(int), 5, file);

    if (elements_read != 5) {
        if (feof(file)) {
            printf("Достигнут конец файла\n");
        } else {
            perror("Ошибка чтения");
        }
    }

    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);  // Выведет: 10 20 30 40 50
    }

    fclose(file);
    return 0;
}
```

## 121212
```C
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int numbers[10] = { 1, 0, -2, 3, 10, 4, 3, 2, 3, 9 };
    int offset;
    FILE *fp = fopen("intarray", "w+b");
    if (!fp) {
        fprintf(stderr, "Could not open file\n");
        return EXIT_FAILURE;
    }
    // write to the file
    size_t n = fwrite(numbers, sizeof(int), 10, fp);
    if (ferror(fp)) {
        fprintf(stderr, "Error occurred\n");
        return EXIT_FAILURE;
    }
    fprintf(stdout, "%lu items written\n", n);  // same as printf
    // flush to the file from the stream buffer
    fflush(fp);

    // get the file offset
    offset = ftell(fp);
    printf("Current file position indicator is %d\n", offset);
    // set the offset to the beginning of the files
    fseek(fp, 0, SEEK_SET);
    offset = ftell(fp);
    printf("Current file position indicator after fseek is %d\n", offset);
    // set the offset to the beginning of the files
    rewind(fp);
    offset = ftell(fp);
    printf("Current file position indicator after rewind is %d\n", offset);
    // read the integers
    int *num2 = (int*)malloc(10 * sizeof(int));
    n = fread(num2, sizeof(int), 10, fp);

    // feof indicator should not be set yet, because we did not read
    // past the end of file
    if (feof(fp)) {
        fprintf(stderr, "prematurely reached end of file\n");
        return EXIT_FAILURE;
    } else if (ferror(fp)) {
        fprintf(stderr, "error occurred\n");
        return EXIT_FAILURE;
    }
    fprintf(stdout, "%lu items read, EOF indicator is not set\n", n);

    // should not read anything, because we should be at the end of file
    n = fread(num2, sizeof(int), 10, fp);
    if (feof(fp)) {
        fprintf(stdout, "%lu items read, EOF indicator is set\n", n);
    }

    // set the offset after the first element
    fseek(fp, sizeof(int), SEEK_SET);
    offset = ftell(fp);
    printf("Current file position indicator after fseek is %d\n", offset);
    n = fread(num2, sizeof(int), 10, fp);
    if (feof(fp)) {
        fprintf(stdout, "%lu items read, EOF indicator is set\n", n);
    }

    fclose(fp);
    free(num2);
    return EXIT_SUCCESS;
}
```

---

# Аргументы командной строки
```C
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Total arguments: %d\n", argc);
    
    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    
    return 0;
}
```

- Вызов программы выглядит как:
	`./myprogram hello world 123`

# Чтение строки
```C
#include <stdio.h>

int main() {
    char str[100]; // Объявляем массив для хранения строки

    printf("Введите строку: ");
    fgets(str, sizeof(str), stdin); // Читаем строку с клавиатуры

    printf("Вы ввели: %s", str); // Выводим введенную строку

    return 0;
}
```
