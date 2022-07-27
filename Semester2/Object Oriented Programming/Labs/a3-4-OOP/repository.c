#include "repository.h"
#include "domain.h"
#include "dynamicArray.h"
#include <string.h>
#include <stdlib.h>
#include <assert.h>

Repo* createRepo(int capacity)
{
    Repo* r = malloc(sizeof(Repo) );
    if (r == NULL)
        return NULL;
    r->vector = createVector(capacity);

    return r;
}

void destroyRepo(Repo* r)
{
    if(r == NULL)
        return;

    destroyVector(r->vector);
    free(r);
}

int getLengthRepo(Repo* r)
{
    return r->vector->size;
}

int sameId(Product* p1, Product* p2)
{
    if(strcmp(p1->name, p2->name) == 0 && (strcmp(p1->category, p2->category) == 0))
        return 1;
    return 0;
}

void swapProducts(Product *a, Product *b)
{
    Product aux = *a;
    *a = *b;
    *b = aux;
}

Product* getProductOnPos(Repo * r, int pos)
{
    if (r == NULL)
        return NULL;
    if (pos < 0 || pos >= getLengthRepo(r))
        return NULL;
    return r->vector->data[pos];
}

int getPosOfProduct(Repo* r, Product* p)
{
    if(r == NULL)
        return -1;
    if(p == NULL)
        return -1;

    for(int i = 0; i < r->vector->size; i++)
    {
        if(r->vector->data[i] == p)
            return i;
    }
    return -1;
}

Product* findById(Repo* r, char* name, char* category)
{
    if(r == NULL || name == NULL || category == NULL)
        return NULL;

    for(int i = 0; i < r->vector->size; i++)
    {
        Product* p = get(r->vector, i);
        if(strcmp(getName(p), name) == 0 && strcmp(getCategory(p), category) == 0)
            return p;
    }

    return NULL;
}


int addRepo(Repo* r, Product* p)
{
    int ok = 1;
    if (r == NULL || p == NULL)
        return -1;

    for (int i = 0; i < getLengthRepo(r); i++)
    {
        if(sameId(r->vector->data[i], p) == 1) {
            int quantity = getQuantity(r->vector->data[i]);
            setQuantity(r->vector->data[i], quantity + p->quantity);
            ok = 0;
        }
    }
    if(ok == 1)
        addToVector(r->vector, p);
    return ok;
}

int removeRepo(Repo* r, char* name, char* category)
{
    if(r == NULL || name == NULL || category == NULL)
        return -1;
    Product* p = findById(r, name, category);
    for(int i = 0; i < r->vector->size; i++)
    {
        if(get(r->vector, i) == p)
        {
            removeFromVector(r->vector, i);
            return 1;
        }
    }
    return 0;
}

int updateRepo(Repo* r, char* name, char* category, int newQuantity, int newDate)
{
    if (r == NULL || name == NULL || category == NULL)
        return 0;

    Product* p = findById(r, name, category);
    int pos = getPosOfProduct(r, p);
    if(pos == -1)
        return 0;

    setQuantity(r->vector->data[pos], newQuantity);
    setDate(r->vector->data[pos], newDate);

    return 1;

}

void initProductRepoTest(Repo* r)
{
    Product* p = createProduct("chicken", "meat", 12, 2002);
    addRepo(r, p);
}

void testAdd()
{
    Repo* r = createRepo(10);
    initProductRepoTest(r);
    assert(getLengthRepo(r) == 1);
    Product* p = createProduct("pork", "meat", 10, 2002);
    assert(addRepo(r, p) == 1);
    assert(getLengthRepo(r) == 2);
    assert(addRepo(r, p) == 0);
    destroyRepo(r);

}


void testRemove()
{
    Repo* r = createRepo(10);
    initProductRepoTest(r);
    assert(getLengthRepo(r) == 1);
    assert(removeRepo(r, "chicken", "meat") == 1);
    assert(getLengthRepo(r) == 0);
    assert(removeRepo(r, "chicken", "idk") == 0);
    destroyRepo(r);

}

void testUpdate()
{
    Repo* r = createRepo(10);
    initProductRepoTest(r);
    assert(updateRepo(r, "chicken", "meat", 15, 10) == 1);
    assert(updateRepo(r, "chicken", "idk", 15, 15) == 0);
    assert(getQuantity(r->vector->data[0]) == 15);
    destroyRepo(r);
}

void testRepo()
{
    testAdd();
    testRemove();
    testUpdate();
}
