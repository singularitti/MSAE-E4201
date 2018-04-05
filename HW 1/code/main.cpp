#include <iostream>
#include <cmath>

int main() {
    double x, y, z, v, l_square, i = 0;
    double xp, yp, zp;
    for (xp = 0; xp < 2; xp += 0.01) {
        for (yp = 0; yp < 2; yp += 0.01) {
            for (zp = 0; zp < 2; zp += 0.01) {
                for (x = -60 + xp; x <= 60 + xp; x += 2) {
                    for (y = -60 + yp; y <= 60 + yp; y += 2) {
                        for (z = -60 + zp; z <= 60 + zp; z += 2) {
                            l_square = pow(x - xp, 2.0) + pow(y - yp, 2.0) + pow(z - zp, 2.0);
                            if (2500 <= l_square && l_square <= 3600) i += 1;
                        }
                    }
                }
            }
        }
    }
    printf("%f", i);
}
