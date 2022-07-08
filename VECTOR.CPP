#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
int main() {
int rn, kl, x, y, q;
cin >> rn >> q;
int *val[rn];
for (int i = -1; ++i < rn;) {
    cin >> kl;
    val[i] = new int[kl];
    for (int j = -1; ++j < kl; cin >> val[i][j]);
}
while(q--){
    cin >> x >> y;
    cout << val[x][y] << endl;
}
    return 0;
}
    return 0;
}