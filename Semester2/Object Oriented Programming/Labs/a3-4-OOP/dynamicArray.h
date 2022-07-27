#pragma once
#include "domain.h"

typedef Product TElem;

typedef struct
{
    TElem** data;
    int size, capacity;
} Vector;


/// Creates a vector
/// \param capacity The capacity of the vector
/// \return The vector
Vector* createVector(int capacity);


/// This function is used to deallocate the memory used for the vector
/// \param v The vector
void destroyVector(Vector* v);


/// This function is used to increase the capacity of the vector in case we need it
/// \param v The vector
void resize(Vector* v);


/// This function is used to add a TElem to the vector
/// \param v The vector
/// \param el The element
void addToVector(Vector* v, TElem* el);


/// This function is used to remove a TElem from the a certain position of a vector
/// \param v The vector
/// \param pos The position
void removeFromVector(Vector* v, int pos);

/// This function is used to get a TElem from a certain position of a vector
/// \param v The vector
/// \param pos The position
/// \return The element from the position pos
TElem* get(Vector* v, int pos);

/// This function is used to create a copy of a vector
/// \param v The vector
/// \return Its copy
Vector* makeCopy(Vector* v);


///This function is used to test the vector
void testVector();