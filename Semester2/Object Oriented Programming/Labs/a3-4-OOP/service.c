#include "service.h"
#include <stdlib.h>
#include <string.h>
#include <assert.h>

Service* createService(Repo * repo)
{
    Service* s = (Service*)malloc(sizeof(Service));

    if (s == NULL)
        return NULL;

    s->repo = repo;

    return s;
}

void destroyService(Service* s)
{
    if (s == NULL)
        return;

    destroyRepo(s->repo);

    free(s);
}


Repo* getRepo(Service* s)
{
    if (s == NULL)
        return NULL;
    return s->repo;
}

int addService(Service* s, char* name, char* category, int quantity, int date)
{
    if(s == NULL)
        return -1;

    if(name == NULL || category == NULL)
        return -1;
    Product* p = createProduct(name, category, quantity, date);

    if(p == NULL)
        return -1;

    int res = addRepo(s->repo, p);
    if(res == 0)
        destroyProduct(p);

    return res;
}

int removeService(Service* s, char* name, char* category)
{
    if(s == NULL || name == NULL || category == NULL)
        return -1;

    return removeRepo(s->repo, name, category);
}

int updateService(Service* s, char* name, char* category, int newQuantity, int newDate) {
    if (s == NULL || name == NULL || category == NULL)
        return -1;

    return updateRepo(s->repo, name, category, newQuantity, newDate);
}

typedef int (*sort)(Product* p1, Product* p2);

typedef int (*filter)(Product* p, int quantity);

int filterByQuantity(Product* p, int quantity)
{
    if(p->quantity > quantity)
        return 1;
    return 0;
}

int sortingAscendingByQuantity(Product* p1, Product* p2)
{
    if(p1->quantity < p2->quantity)
        return 1;
    return 0;
}

int sortingAscendingByDate(Product* p1, Product* p2)
{
    if(p1->date < p2->date)
        return 1;
    return 0;
}

int sortingDescendingByDate(Product* p1, Product* p2)
{
    if(p1->date > p2->date)
        return 1;
    return 0;
}

void sortVector(Vector* result, int(*sort)(Product* p1, Product* p2)) {
    int i, j;

    for (i = 0; i < result->size - 1; i++) {
        for (j = i + 1; j < result->size; j++) {
            if ((*sort)(result->data[i], result->data[j]) == 0)
            {
                Product *aux = result->data[i];
                result->data[i] = result->data[j];
                result->data[j] = aux;
            }
        }
    }
}



int filterForPrinting(Service* s, char* filter, Vector* result)
{
    if (s == NULL)
        return 0;

    int i;
    if (filter[0] == '\0')
    {
        for (i = 0; i < s->repo->vector->size; i++)
        {
            Product* p = createProduct(s->repo->vector->data[i]->name, s->repo->vector->data[i]->category, s->repo->vector->data[i]->quantity, s->repo->vector->data[i]->date);
            addToVector(result, p);
        }
    }
    else
    {
        for (i = 0; i < s->repo->vector->size; i++) {
            char *found;
            found = strstr(s->repo->vector->data[i]->name, filter);
            if (found != NULL) {
                Product *product = createProduct(getName(s->repo->vector->data[i]),
                                                 getCategory(s->repo->vector->data[i]),
                                                 getQuantity(s->repo->vector->data[i]),
                                                 getDate(s->repo->vector->data[i]));
                addToVector(result, product);
            }

        }
    }
    sort sort = &sortingAscendingByQuantity;
    sortVector(result, sort);

    return 1;
}

//This is for b bonus
int filterVectorBonus(Service* s, int quantity, Vector* result,int (*filter)(Product* p, int quantity))
{
    if (s == NULL)
        return 0;
    int i;

    for(i = 0; i < s->repo->vector->size;i++)
    {
        if((*filter)(s->repo->vector->data[i], quantity) == 1)
        {
            Product *product = createProduct(getName(s->repo->vector->data[i]),
                                             getCategory(s->repo->vector->data[i]),
                                             getQuantity(s->repo->vector->data[i]),
                                             getDate(s->repo->vector->data[i]));
            addToVector(result, product);
        }
    }
    return 1;

}

int getFilterBonus(Service* s, int quantity, Vector* result)
{
    if(s == NULL)
        return 0;
    filter filter = &filterByQuantity;
    int res = filterVectorBonus(s, quantity, result, filter);
    return res;
}
//This is for bonus b

int searchProductByCategoryAscending(Service* s, char* category, int expirationDate, int x, Vector* result)
{
    if(s == NULL)
        return -1;

    int i;
    for(i = 0; i < s->repo->vector->size; i++)
    {
        if(strcmp(s->repo->vector->data[i]->category, category) == 0 && (s->repo->vector->data[i]->date - expirationDate) < x && (s->repo->vector->data[i]->date - expirationDate) > 0)
        {
            Product* p = createProduct(s->repo->vector->data[i]->name, s->repo->vector->data[i]->category, s->repo->vector->data[i]->quantity, s->repo->vector->data[i]->date);
            addToVector(result, p);
        }
    }

    sort sort = &sortingAscendingByDate;
    sortVector(result, sort);

    return 1;
}

int searchProductByCategoryDescending(Service* s, char* category, int expirationDate, int x, Vector* result)
{
    if(s == NULL)
        return -1;

    int i;
    for(i = 0; i < s->repo->vector->size; i++)
    {
        if(strcmp(s->repo->vector->data[i]->category, category) == 0 && (s->repo->vector->data[i]->date - expirationDate) < x && (s->repo->vector->data[i]->date - expirationDate) > 0)
        {
            Product* p = createProduct(s->repo->vector->data[i]->name, s->repo->vector->data[i]->category, s->repo->vector->data[i]->quantity, s->repo->vector->data[i]->date);
            addToVector(result, p);
        }
    }

    sort sort = &sortingDescendingByDate;
    sortVector(result, sort);

    return 1;
}

//This is bonus c

void testAddService()
{
    Repo* r = createRepo(10);
    Service* s = createService(r);

    assert(getLengthRepo(r) == 0);

    assert(addService(s, "idk", "idk", 100, 1000) == 1);
    assert(addService(s, "idk", "idk", 1000, 1) == 0);

    assert(getLengthRepo(r) == 1);

    destroyService(s);

}

void testDeleteService()
{
    Repo* r = createRepo(10);
    Service* s = createService(r);

    assert(getLengthRepo(r) == 0);
    assert(addService(s, "idk", "idk", 100, 1000) == 1);
    assert(getLengthRepo(r) == 1);

    assert(removeService(s, "idk", "idk") == 1);
    assert(getLengthRepo(r) == 0);

    assert(removeService(s, "idk", "idk") == 0);
    assert(removeService(s, "idk1", "idk1") == 0);

    destroyService(s);

}

void testUpdateService()
{
    Repo* r = createRepo(10);
    Service* s = createService(r);

    assert(getLengthRepo(r) == 0);
    assert(addService(s, "idk", "idk", 100, 1000) == 1);
    assert(getLengthRepo(r) == 1);

    assert(updateService(s, "idk", "idk", 10, 10) == 1);

    assert(removeService(s, "idk", "idk") == 1);
    assert(getLengthRepo(r) == 0);

    assert(updateService(s, "idk", "idk", 10, 10) == 0);

    destroyService(s);

}

void testService()
{
    testAddService();
    testDeleteService();
    testUpdateService();
}