#include <stdio.h>
#include "stock.h"

#define MAX_STOCK 100

int purchase(int qty)
{
    if(getstock() + qty <= MAX_STOCK)
    {
        addstock(qty);
        printf("Purchase successful\n");
        return 1;
    }
    else
    {
        printf("Stock full. Cannot purchase\n");
        return 0;
    }
}
