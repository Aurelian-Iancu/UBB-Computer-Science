#include "dynamicArray.h"
#include "domain.h"
#include <stdlib.h>
#include <assert.h>

Vector* createVector(int capacity)
{
    Vector* v = (Vector*)malloc(sizeof(Vector));

    if (v == NULL)
        return NULL;

    v->capacity = capacity;
    v->size = 0;
    v->data = (TElem**)malloc(v->capacity * sizeof(TElem*));

    if (v->data == NULL)
    {
        free(v);
        return NULL;
    }

    return v;
}

void destroyVector(Vector* v)
{
    if (v == NULL)
        return;

    if (v->data == NULL)
    {
        free(v);
        return;
    }

    int i;
    for (i = 0; i < v->size; i++)
    {
        if (v->data[i] != NULL)
            destroyProduct(v->data[i]);
    }

    free(v->data);
    free(v);
}

void resize(Vector* v)
{
    if (v == NULL)
        return;

    v->capacity *= 2;

    TElem** aux = (TElem**)realloc(v->data, v->capacity * sizeof(TElem*));
    if (aux == NULL)
        return;

    v->data = aux;
}

void addToVector(Vector* v, TElem* el)
{
    if (v == NULL || el == NULL)
        return;

    if (v->size == v->capacity)
        resize(v);

    v->data[v->size] = el;
    v->size++;
}

void removeFromVector(Vector* v, int pos)
{
    if (v == NULL || pos < 0 || pos >= v->size)
        return;

    int i;
    for (i = pos; i < v->size - 1; i++)
    {
        v->data[i] = v->data[i + 1];
    }
    v->data[v->size - 1] = NULL;
    v->size--;
}

TElem* get(Vector* v, int pos)
{
    if(v == NULL || pos < 0)
        return NULL;
    return v->data[pos];
}

Vector* makeCopy(Vector* v)
{
    Vector* newVector = createVector(v->capacity);
    if (newVector == NULL)
        return NULL;

    int i;
    for (i = 0; i < v->size; i++)
    {
        Product* p = createProduct(v->data[i]->name, v->data[i]->category, v->data[i]->quantity, v->data[i]->date);
        if (p == NULL)
        {
            destroyVector(newVector);
            return NULL;
        }

        addToVector(newVector, p);
    }

    return newVector;
}


// TESTS
void testAddToVector()
{
    Vector* v = createVector(10);

    assert(v->size == 0);

    Product* p = createProduct("house", "100", 10, 10);
    addToVector(v, p);

    assert(v->size == 1);

    destroyVector(v);
}

void testRemoveFromVector()
{
    Vector* v = createVector(10);

    assert(v->size == 0);

    Product* p = createProduct("house", "100", 10, 10);
    addToVector(v, p);

    assert(v->size == 1);

    removeFromVector(v, 0);

    assert(v->size == 0);

    destroyVector(v);
}

void testGetFromVector()
{
    Vector* v = createVector(10);

    assert(v->size == 0);

    Product* p = createProduct("house", "100", 10, 10);
    addToVector(v, p);

    assert(get(v, 0) == p);


    destroyVector(v);
}

void testMakeCopy()
{
    Vector* v = createVector(10);

    assert(v->size == 0);

    Product* p = createProduct("house", "100", 10, 10);
    addToVector(v, p);

    assert(v->size == 1);

    Vector* vCopy = makeCopy(v);
    assert(vCopy->size == 1);

    removeFromVector(v, 0);

    assert(v->size == 0);
    assert(vCopy->size == 1);

    destroyVector(v);
    destroyVector(vCopy);
}

void testVector()
{
    testAddToVector();
    testRemoveFromVector();
    testGetFromVector();
    testMakeCopy();
}