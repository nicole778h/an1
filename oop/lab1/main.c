#include <stdio.h>
#include <stdlib.h>
//Determina intersectia a doua segmente plane (date prin coordonatelelor carteziene).


int main()
{int x1,y1,x2,y2,x3,y3,x4,y4,x,y,m1,n1,m2,n2,min1,max1,min2,max2,min3,max3,min4,max4;
printf("x1= ");
scanf("%d",&x1);
printf("y1= ");
scanf("%d",&y1);
printf("x2= ");
scanf("%d",&x2);
printf("y2= ");
scanf("%d",&y1);
printf("x3= ");
scanf("%d",&x3);
printf("y3= ");
scanf("%d",&y3);
printf("x4= ");
scanf("%d",&x4);
printf("y4= ");
scanf("%d",&y4);

if(x1==x2|| x3==x4);
    printf("cel putin o dreapta este paralela cu oy ");
else
{
    m1=(y2-y1)/(x2-x1);
    m2=(y4-y3)/(x4-x3);
    n1=y1-m1*x1;
    n2=y3-m2*m3;
    if(m1==m2);
    {
        if(y1==m2*x1+n2);
            printf("segmentele sunt pe aceeasi dreapta");
        else
            printf("segmentele sunt paralele");
    }
    else
    {
        x=(n2-n1)/(m1-m2);
        y=m1*x+n1;
        if(x1<x2);{min1=x1; max1=x2;}
        else {min1=x2; max2=x1}
        if(y1<y2); {min2=y1; max2=y2;}
        else {min2=y2; max2=y1;}
        if(x3<x4) {min3=x3; max3=x4;}
        else {min3=x4; max3=x3;}
        if(y3<y4) {min4=y3; max4=y4;}
        else {min4=y4; max4=y3;}
        if(x<min1|| y<min2|| x<min3|| y<min4|| x?max1|| y>max2|| x>max3|| y>max4);
            printf("segmentele se intersecteaza in prelungiriile");
            scanf("%d",&x);
            scanf("%d", &y);

    }
}


    return 0;
}




//problema 9
// Citeste un sir de numere naturale nenule terminat cu 0 si determina
//numarul cifrelor 0 in care se termina numarul produs al numerelor citite.

void p9();
int min(a, b);

int main()
{
    p9();
    return 0;
}

int min(a, b)
{
    if (b < a)
        return b;
    return a;
}

void p9()
{
    int n, nr2 = 0, nr5 = 0;

    do
    {
        scanf("%d", &n);
        while (n % 2 == 0 && n != 0)
        {
            nr2++;
            n /= 2;
        }

        while (n % 5 == 0 && n != 0)
        {
            nr5++;
            n /= 5;
        }


    } while (n);


    printf("%d", min(nr2, nr5));
}