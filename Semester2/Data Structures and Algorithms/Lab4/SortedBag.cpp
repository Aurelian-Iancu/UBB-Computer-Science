#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <cmath>

int SortedBag::hCode(TComp k) {
    return abs(k);
}
///theta(1)


int SortedBag::h1(TComp k) const{
    return hCode(k) % this->capacity;
}
///theta(1)


int SortedBag::h2(TComp k) const {
    return 1+(hCode(k)%(this->capacity-1));
}
///theta(1)

int SortedBag::h(TComp k, int i) const{
    return (h1(k) + i * h2(k)) % this->capacity;
}
///theta(1)

bool SortedBag::prim(int x) {
    if(x < 2 || (x > 2 && x % 2 == 0))
        return false;
    for(int d = 3; d * d <= x; d = d + 2)
        if(x % d == 0)
            return false;
    return true;
}
///O(sqrt(x))

int SortedBag::firstPrimeGreaterThan(int n) {
    n++;
    while (!prim(n))
        n++;
    return n;
}
///O(n)

SortedBag::SortedBag(Relation r) {
	this->relation = r;
    this->capacity = maxCapacity;
    this->length = 0;
    this->empty = -1111;
    this->deleted = -1112;
    this->hashTable = new TElem [maxCapacity];
    for(int i = 0; i < maxCapacity; i++)
        this->hashTable[i] = this->empty;
}
///theta(capacity)

void SortedBag::add(TComp e) {
    if(this->length == this->capacity)
    {
        ///We resize and rehash if we don't have anymore space in the hashTable
        int prime = firstPrimeGreaterThan(this->capacity * 2);
        int oldCap = this->capacity;
        this->capacity = prime;
        TComp *oldTable = this->hashTable;
        this->hashTable = new TElem [capacity];
        this->length = 0;
        for(int j = 0; j < this->capacity; j++)
        {
            this->hashTable[j] = this->empty;
        }
        for(int j = 0; j < oldCap; j++)
        {
            this->add(oldTable[j]);
        }
        delete[] oldTable;
    }

    int i = 0;
    int pos = h(e, i);
    while (i < this->capacity && this->hashTable[pos] != this->empty && this->hashTable[pos] != this->deleted)
    {
        i++;
        pos = h(e,i);
    }
    this->hashTable[pos] = e;
    this->length++;
}
///BC: theta(1), WC: theta(nrElements ^ 2), Overall: O(nrElements ^ 2)


bool SortedBag::remove(TComp e) {
	int i = 0;
    int pos = h(e, i);
    while(i < this->capacity && this->hashTable[pos] != e && this->hashTable[pos] != this->empty)
    {
        i++;
        pos = h(e,i);
    }
    if(i == this->capacity || this->hashTable[pos] == this->empty)
        return false;

    this->hashTable[pos] = this->deleted;
    this->length--;
    return true;
}
///BC: theta(1), WC: theta(nrElements), Total complexity: O(nrElements)


bool SortedBag::search(TComp elem) const {
	int i = 0;
    int pos = h(elem, i);
    while(i < this->capacity && this->hashTable[pos] != elem && this->hashTable[pos] != this->empty)
    {
        i++;
        pos = h(elem, i);
    }
    if(i == this->capacity || this->hashTable[pos] == this->empty)
        return false;
    return true;
}
///BC: theta(1), WC: theta(nrElements), Total complexity: O(nrElements)



int SortedBag::nrOccurrences(TComp elem) const {
	int nrOccurences = 0;
    int i = 0;
    int pos = h(elem,i);
    while(i < this->capacity && this->hashTable[pos] != this->empty){
        if(this->hashTable[pos] == elem){
            nrOccurences++;
        }
        i++;
        pos = h(elem, i);
    }
    return nrOccurences;
}
///theta(nrElements)



int SortedBag::size() const {
	return this->length;
}
///theta(1)


bool SortedBag::isEmpty() const {
	return this->length == 0;
}
///theta(1)


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}
///theta(1)


SortedBag::~SortedBag() {
	delete[] this->hashTable;
}
///theta(1)








