#include <cstdlib>
#include <iostream>
#include <vector>

bool single_bits_test(std::vector<bool> bits)
{
    int n = bits.size();
    int ones = 0;
    for (int i = 0; i < n; i++)
    {
        if (bits[i])
        {
            ones++;
        }
    }
    return (ones > 9725) && (ones < 10275);
}

bool poker_test(std::vector<bool> bits)
{
    int n = bits.size();
    int m = n / 4;
    int k = 0;
    int f[16] = {0};

    for (int i = 0; i < m; i++)
    {
        int sum = 0;
        for (int j = 0; j < 4; j++)
        {
            sum += bits[i * 4 + j] * (1 << (3 - j));
        }
        f[sum]++;
    }

    for (int i = 0; i < 16; i++)
    {
        k += f[i] * f[i];
    }

    double x = (16.0 / 5000.0) * k - 5000.0;
    std::cout << "Wartosc X:" << x << std::endl;
    return (x < 46.17) && (x > 2.16);
}

bool series_test(std::vector<bool> bits)
{
    int n = bits.size();

    int ones = 0;
    int double_ones = 0;
    int triple_ones = 0;
    int quad_ones = 0;
    int quint_ones = 0;
    int max_ones = 0;

    int zeros = 0;
    int double_zeros = 0;
    int triple_zeros = 0;
    int quad_zeros = 0;
    int quint_zeros = 0;
    int max_zeros = 0;

    int pom_ones = 0;
    int pom_zeros = 0;

    for (int i = 0; i < n; i++)
    {
        if (bits[i])
        {
            pom_ones++;

            if (pom_zeros > 0)
            {
                if (pom_zeros == 1)
                {
                    zeros++;
                }
                else if (pom_zeros == 2)
                {
                    double_zeros++;
                }
                else if (pom_zeros == 3)
                {
                    triple_zeros++;
                }
                else if (pom_zeros == 4)
                {
                    quad_zeros++;
                }
                else if (pom_zeros == 5)
                {
                    quint_zeros++;
                }
                else
                {
                    max_zeros++;
                }

                pom_zeros = 0;
            }
        }
        else
        {
            pom_zeros++;

            if (pom_ones > 0)
            {
                if (pom_ones == 1)
                {
                    ones++;
                }
                else if (pom_ones == 2)
                {
                    double_ones++;
                }
                else if (pom_ones == 3)
                {
                    triple_ones++;
                }
                else if (pom_ones == 4)
                {
                    quad_ones++;
                }
                else if (pom_ones == 5)
                {
                    quint_ones++;
                }
                else
                {
                    max_ones++;
                }

                pom_ones = 0;
            }
        }
    }
    return (ones < 2685) && (ones > 2315) && (double_ones < 1386) && (double_ones > 1114) && (triple_ones < 723) && (triple_ones > 527) && (quad_ones < 384) && (quad_ones > 240) && (quint_ones < 209) && (quint_ones > 103) && (max_ones < 209) && (max_ones > 103) && (zeros < 2685) && (zeros > 2315) && (double_zeros < 1386) && (double_zeros > 1114) && (triple_zeros < 723) && (triple_zeros > 527) && (quad_zeros < 384) && (quad_zeros > 240) && (quint_zeros < 209) && (quint_zeros > 103) && (max_zeros < 209) && (max_zeros > 103);
}