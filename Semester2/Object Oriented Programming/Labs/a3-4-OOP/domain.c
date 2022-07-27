#include "domain.h"
#include <string.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

Product* createProduct(char* name, char* category, int quantity, int date) {
    Product* p = malloc(sizeof(Product));
    if(p == NULL)
        return NULL;

    p->name = malloc(sizeof(char) * strlen(name) + 1);
    if(p->name != NULL)
        strcpy(p->name, name);

    p->category = malloc(sizeof(char) * strlen(category) + 1);
    if(p->category != NULL)
        strcpy(p->category, category);

    p->quantity = quantity;

    p->date = date;

    return p;

}

void destroyProduct(Product* p)
{
    if(p == NULL)
        return;

    free(p->name);
    free(p->category);

    free(p);
}

const char* getName(Product* p)
{
    if(p == NULL)
        return NULL;
    return p->name;
}

const char* getCategory(Product* p)
{
    if(p == NULL)
        return NULL;
    return p->category;
}

int getQuantity(Product* p)
{
    if(p == NULL)
        return -1;
    return p->quantity;
}

int getDate(Product* p)
{
    if(p == NULL)
        return -1;
    return p->date;
}

void setName(Product* p, char* name)
{
    free(p->name);
    p->name = (char*)malloc((strlen(name) + 1) * sizeof(char));
    strcpy(p->name, name);
}

void setCategory(Product* p, char* category)
{
    free(p->category);
    p->category = (char*)malloc((strlen(category) + 1) * sizeof(char));
    strcpy(p->category, category);
}

void setQuantity(Product* p, int otherQuantity)
{
    p->quantity = otherQuantity;

}

void setDate(Product* p, int otherDate)
{
    p->date = otherDate;
}

void toString(Product* p, char str[])
{
    if(p == NULL)
    {
        return;
    }
    sprintf(str, "Product %s (%s) has quantity %d and date expiration %d.", p->name, p->category, p->quantity, p->date);
}


void testProduct()
{
    Product* p = createProduct("chicken", "meat", 12, 2022);
    assert(strcmp(p->name, "chicken") == 0);
    assert(strcmp(p->category, "meat") == 0);
    assert(p->quantity == 12);
    assert(p->date == 2022);
    assert(strcmp(getName(p), "chicken") == 0);
    assert(strcmp(getCategory(p), "meat") == 0);
    assert(getQuantity(p) == 12);
    assert(getDate(p) == 2022);
    setName(p, "pork");
    assert(strcmp(getName(p), "pork") == 0);
    setCategory(p, "meat1");
    assert(strcmp(getCategory(p), "meat1") == 0);
    setQuantity(p, 10);
    assert(getQuantity(p) == 10);
    setDate(p, 2020);
    assert(getDate(p) == 2020);

    destroyProduct(p);



}



