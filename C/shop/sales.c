#include <stdio.h>
#include "stock.h"

int sell(int qty)
{
    if(getstock() >= qty)
    {
        deletestock(qty);
        printf("Sale successful\n");
        return 1;
    }
    else
    {
        printf("Not enough stock\n");
        return 0;
    }
}
