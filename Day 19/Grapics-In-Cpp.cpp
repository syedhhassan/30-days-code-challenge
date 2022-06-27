#include <graphics.h>
int main()
{
    int gd= DETECT, gm;
    int l=180, t=180;
    int r=500, b=500;
    initgraph(&gd, &gm, "");
    rectangle(l,t,r,b)
    getch():
    closegraph();
    return 0;
}