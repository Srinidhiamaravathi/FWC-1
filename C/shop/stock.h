#ifndef STOCK_H
#define STOCK_H

extern int stock;

void addstock(int qty);
void deletestock(int qty);
int getstock();

int sell(int qty);
int purchase(int qty);

#endif
