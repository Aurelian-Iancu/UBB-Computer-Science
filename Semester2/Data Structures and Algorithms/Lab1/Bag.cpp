#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
#include <exception>
using namespace std;

Bag::Bag() {
    this->capacity = 10;
    this->nrElements = 0;
    this->elements = new TElem[capacity];
    this->frequency = new int[capacity];
}
///Theta(1)


void Bag::resize()
{
    this->capacity *= 2;
    TElem* aux1,* aux2;
    aux1 = new TElem[capacity];
    aux2 = new TElem[capacity];
    for(int i = 0; i < this->nrElements; i++)
    {
        aux1[i] = this->elements[i];
        aux2[i] = this->frequency[i];
    }
    delete[] this->elements;
    delete[] this->frequency;
    this->elements = aux1;
    this->frequency = aux2;

}
///Theta(nrElements)

void Bag::add(TElem elem) {

    int found = 0;
    int index = 0;
    while(index < nrElements && found == 0)
    {
        if(this->elements[index] == elem)
        {
            found = 1;
            this->frequency[index]++;
        }
        index++;
    }
    if(found == 0)
    {
        this->elements[nrElements] = elem;
        this->frequency[nrElements] = 1;
        nrElements++;
    }
    if(this->capacity-1 == this->nrElements)
        resize();
}
///Best case: Theta(1), Worst case: Theta(nrElements) => Total complexity: O(nrElements)


bool Bag::remove(TElem elem) {
	int index = 0;
    int aux;
    while(index < this->nrElements)
    {
        if(this->elements[index] == elem)
        {
            if(this->frequency[index] > 1)
                this->frequency[index] -= 1;
            else
            {
                aux = this->elements[nrElements-1];
                this->elements[nrElements-1] = this->elements[index];
                this->elements[index] = aux;

                aux = this->frequency[nrElements-1];
                this->frequency[nrElements-1] = this->frequency[index];
                this->frequency[index] = aux;

                nrElements--;
            }
            return true;
        }
        index++;
    }
	return false; 
}
///Best case: Theta(1), Worst case: Theta(nrElements) => Total complexity: O(nrElements)

bool Bag::search(TElem elem) const {
	int index = 0;
    while(index < this->nrElements)
    {
        if(this->elements[index] == elem)
            return true;
        index++;
    }
	return false; 
}
///Best case: Theta(1), Worst case: Theta(nrElements) => Total complexity: O(nrElements)

int Bag::nrOccurrences(TElem elem) const {
	int index = 0;
    while(index < this->nrElements)
    {
        if(this->elements[index] == elem)
            return this->frequency[index];
        index++;
    }
	return 0; 
}
///Best case: Theta(1), Worst case: Theta(nrElements) => Total complexity: O(nrElements)


int Bag::size() const {
	int counter = 0;
    for(int i = 0; i < this->nrElements; i++)
        counter+= this->frequency[i];
    return counter;
}
///Theta(nrElements)


bool Bag::isEmpty() const {
	if(this->nrElements == 0) {
        return true;
    }
    return false;
}
///Theta(1)

int Bag::removeOccurrences(int nr, TElem elem)
{
    int index = 0;
    int aux;
    if(nr < 0)
        throw exception();
    while(index < this->nrElements) {
        if (this->elements[index] == elem) {
            if (nrOccurrences(this->elements[index]) > nr) {
                this->frequency[index] -= nr;
                return nr;
            }
            else
            {
                int saved;
                saved = this->frequency[index];
                aux = this->elements[nrElements-1];
                this->elements[nrElements-1] = this->elements[index];
                this->elements[index] = aux;

                aux = this->frequency[nrElements-1];
                this->frequency[nrElements-1] = this->frequency[index];
                this->frequency[index] = aux;

                nrElements--;
                return saved;
            }
        }
        index++;
    }
    return 0;
}
///Best case: Theta(1), Worst case: Theta(nrElements) => Total complexity: O(nrElements)


BagIterator Bag::iterator() const {
	return BagIterator(*this);
}
///Theta(1)

Bag::~Bag(){
    delete[] this->elements;
    delete[] this->frequency;
}
///Theta(1)

