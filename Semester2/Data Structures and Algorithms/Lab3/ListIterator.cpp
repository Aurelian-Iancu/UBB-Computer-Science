#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <exception>

using namespace std;

ListIterator::ListIterator(SortedIteratedList& list) : list(list){
    currentIndex = list.dllaList.head;
} /// theta(1)

void ListIterator::first(){
    currentIndex = list.dllaList.head;
} /// theta(1)

void ListIterator::next(){
    if (this->currentIndex == -1)
        throw exception();
    this->currentIndex = this->list.dllaList.next[this->currentIndex];
} /// theta(1)

bool ListIterator::valid() const{
    if (this->currentIndex == -1)
        return false;
    return true;
} /// theta(1)

TComp ListIterator::getCurrent() const{
    if (this->currentIndex == -1)
        throw exception();
    return this->list.dllaList.elements[this->currentIndex];
}
/// theta(1)

TComp ListIterator::remove() {
    if (this->currentIndex == -1)
        throw exception();

    TComp elem = this->list.remove(*this);

    return elem;
}
/// theta(1)
