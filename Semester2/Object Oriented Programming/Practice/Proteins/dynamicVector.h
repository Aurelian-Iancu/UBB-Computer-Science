#pragma once
#include "domain.h"
template <typename TElem>
class DynamicVector {
private:
    unsigned int capacity, size;
    TElem *data;

    void resize();

public:
    ///Constructor
    explicit DynamicVector(int capacity);

    ///Copy constructor
    DynamicVector (const DynamicVector& v);

    ///Function that adds a TElem to the vector(TElem is of type Movie)
    void addVector(const TElem& elem);

    ///Function that removes a TElem from the certain index from of the vector
    void removeVector(unsigned int index);

    ///Function that updates a TElem from a certain index
    void updateVector(int update_index, TElem elem);

    ///This function overwrites the = operator(Now you can assign a vector to the other)
    DynamicVector& operator=(const DynamicVector& v);

    ///Function that returns the capacity of the vector
    int getCapacity() const;

    ///Function that returns the size of the vector
    int getSize() const;

    ///Function that returns the DynamicVector
    TElem * getVector();

    ///Function that overwrites the []operator(Now we can get to the elements of the vector [vector[i]])
    TElem &operator [](unsigned int index);

    ///This is a destructor for the DynamicVector class
    ~DynamicVector();

};

template <typename TElem>
DynamicVector<TElem>::DynamicVector(int capacity) {
    if(capacity <= 0)
    {
        throw "Can t have an array with less than an element!";
    }
    this->capacity = capacity;
    this->size = 0;
    this->data = new TElem[capacity];
}

template <typename TElem>
DynamicVector<TElem>::DynamicVector(const DynamicVector<TElem> &v) {
    this->capacity = v.capacity;
    this->size = v.size;
    this->data = new TElem[this->capacity];
    for(int i = 0; i < this->size; i++)
        this->data[i] = v.data[i];
}

template <typename TElem>
void DynamicVector<TElem>::addVector(const TElem &elem) {
    if(this->capacity == this->size)
        this->resize();
    this -> data[this -> size++] = elem;
}

template <typename TElem>
void DynamicVector<TElem>::removeVector(unsigned int index) {
    for(unsigned int i = index; i < this->size-1; i++)
        this->data[i] = this->data[i+1];
    this->size--;
}

template <typename TElem>
void DynamicVector<TElem>::updateVector(int update_index, TElem elem) {
    this->data[update_index] = elem;
}

template <typename TElem>
void DynamicVector<TElem>::resize() {
    this->capacity += 10;
    auto* newElems = new TElem[this->capacity];
    for (int i = 0; i < this->size; ++i)
        newElems[i] = this->data[i];

    delete[] this->data;
    this->data = newElems;
}

template <typename TElem>
DynamicVector<TElem> &DynamicVector<TElem>::operator=(const DynamicVector<TElem> &v) {
    if(this == &v)
        return *this;

    this->capacity = v.capacity;
    this->size = v.size;

    delete[] this->data;
    this->data = new TElem[this->capacity];
    for(int i = 0; i < this->size; i++)
        this->data[i] = v.data[i];

    return *this;
}

template <typename TElem>
int DynamicVector<TElem>::getCapacity() const {
    return this->capacity;
}

template <typename TElem>
int DynamicVector<TElem>::getSize() const {
    return this->size;
}

template <typename TElem>
TElem * DynamicVector<TElem>::getVector() {
    return this->data;
}

template <typename TElem>
TElem &DynamicVector<TElem>::operator[](unsigned int index) {
    return this->data[index];
}

template <typename TElem>
DynamicVector<TElem>::~DynamicVector<TElem>() {
    delete[] this->data;
}
