#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c)
{
	this->current = 0;
    this->currentFrequency = 1;
}
///Theta(1)

void BagIterator::first() {
	this->current = 0;
    this->currentFrequency = 1;
}
///Theta(1)

void BagIterator::next() {
	if(this->current == this->bag.nrElements)
        throw exception();
    this->currentFrequency++;
    if(this->currentFrequency > this->bag.frequency[this->current])
    {
        this->current++;
        this->currentFrequency = 1;
    }
}
///Theta(1)

bool BagIterator::valid() const {
	if(this->current < this->bag.nrElements)
    {
        return true;
    }
	return false;
}
///Theta(1)

TElem BagIterator::getCurrent() const
{
	if(this->current == this->bag.nrElements)
    {
        throw exception();
    }
    return this->bag.elements[this->current];
}
///Theta(1)