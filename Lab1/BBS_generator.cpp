#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>

// Funkcja sprawdzająca czy dwie liczby są względnie pierwsze
bool are_coprime(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a == 1;
}

// Funkcja generująca listę liczb względnie pierwszych do danej liczby N
std::vector<int> generate_coprimes(int n)
{
    std::vector<int> coprimes;
    for (int i = 2; i < n; ++i)
    {
        if (are_coprime(i, n))
        {
            coprimes.push_back(i);
        }
    }
    return coprimes;
}

bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int find_closest_prime(int start)
{
    int p = start;
    while (true)
    {
        if (is_prime(p) && (p % 4 == 3))
        {
            return p;
        }
        p++;
    }
}

int main()
{
    srand(static_cast<unsigned>(time(0)));
    int p, q;
    std::vector<bool> generated_code;

    // Użytkownik wprowadza dwie liczby p i q
    std::cout << "Podaj dwie liczby p1 i q1 na podstawie, \n ktorych wyznaczone zostnana najblizsze p i q spelniajace warunki: \n";
    std::cin >> p >> q;

    // Znajdź najbliższe liczby pierwsze spełniające warunki
    int closest_p = find_closest_prime(p);
    int closest_q = find_closest_prime(q);

    // Wyświetl wyniki
    std::cout << "Najblizsza liczba pierwsza do p (p = 3 mod 4, p > 1000, p < 10000): " << closest_p << std::endl;
    std::cout << "Najblizsza liczba pierwsza do q (q = 3 mod 4, q > 1000, q < 10000): " << closest_q << std::endl;

    int N = closest_p * closest_q;

    std::cout << "N = " << N << std::endl;

    // Wygeneruj listę liczb względnie pierwszych do N
    std::vector coprimes = generate_coprimes(N);

    // Wylosuj jedną z liczb
    int random_index = rand() % coprimes.size();
    int random_coprime = coprimes[random_index];

    std::cout << "Wylosowana liczba wzglednie pierwsza do N: " << random_coprime << std::endl;

    // Wyznaczenie wartosci poczatkowej generatora BBS
    unsigned long long int x0 = static_cast<long long>(std::pow(random_coprime, 2)) % N;
    std::cout << "Wartosc poczatkowa X0 = " << x0 << std::endl;

    // Generowanie ciagu bitow
    unsigned long long int x2 = 0, pom = x0;
    for (int i = 1; i < 20000; i++)
    {
        bool parzystosc;
        x2 = static_cast<long long>(std::pow(pom, 2)) % N;
        parzystosc = x2 % 2;
        generated_code.push_back(parzystosc);
        pom = x2;
    }

    for (auto i : generated_code)
    {
        std::cout << i;
    }

    return 0;
}