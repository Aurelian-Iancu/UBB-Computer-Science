#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <iostream>
using namespace std;
#include <exception>

SortedIteratedList::SortedIteratedList(Relation r) {
    this->relation = r;
    this->dllaList.capacity = 10;
    this->dllaList.size = 0;
    this->dllaList.elements = new TComp[this->dllaList.capacity]; // array of elements
    this->dllaList.next = new int[this->dllaList.capacity]; // array of next indexes
    this->dllaList.prev = new int[this->dllaList.capacity];
    this->dllaList.head = -1;  // in the head we save the index of the current element from array
    this->dllaList.tail = -1;

    for(int i=0; i<this->dllaList.capacity-1; i++)
        dllaList.next[i] = i+1;  // assign next positions
    this->dllaList.next[this->dllaList.capacity-1] = -1;

    for(int i=1; i<this->dllaList.capacity; i++)
        dllaList.prev[i] = i-1;  // assign prev positions
    this->dllaList.prev[0] = -1;

    this->dllaList.firstEmpty = 0;
} /// theta(nrNodes)

int SortedIteratedList::size() const {
    return this->dllaList.size;
} /// theta(1)

bool SortedIteratedList::isEmpty() const {
    if (this->dllaList.size==0)
        return true;
    return false;
} /// theta(1)

ListIterator SortedIteratedList::first() {
    return ListIterator(*this);
} /// theta(1)

TComp SortedIteratedList::getElement(ListIterator poz) const {
    if (!poz.valid())
        throw exception();
    return poz.getCurrent();
}/// theta(1)

TComp SortedIteratedList::remove(ListIterator& poz) {
    if (!poz.valid())
        throw exception();

    TComp element;
    element = this->dllaList.elements[poz.currentIndex]; // get the element that is removed

    // case 1:  we remove the head
    if (poz.list.dllaList.head == poz.currentIndex){
        this->dllaList.head = this->dllaList.next[this->dllaList.head]; // the next element becomes the head
        this->dllaList.prev[poz.currentIndex] = -1; // there is no more a previous element.

        this->dllaList.next[poz.currentIndex] = this->dllaList.firstEmpty; // first empty becomes the new slot from the old head
        this->dllaList.firstEmpty = poz.currentIndex;

        this->dllaList.size--;
        poz.currentIndex = this->dllaList.head;

        return element;
    }

    // case 2: we remove the tail
    if (poz.list.dllaList.tail == poz.currentIndex){
        this->dllaList.tail = this->dllaList.prev[this->dllaList.tail]; // the previous element becomes the new tail
        this->dllaList.next[this->dllaList.tail] = -1;  // there is no more a next element

        this->dllaList.next[poz.currentIndex] = this->dllaList.firstEmpty; // first empty becomes the new slot from the old tail
        this->dllaList.firstEmpty = poz.currentIndex;

        this->dllaList.size--;
        poz.currentIndex = -1;

        return element;
    }

    // case 3: remove from the middle
    int prev = this->dllaList.prev[poz.currentIndex];
    int next = this->dllaList.next[poz.currentIndex];
    this->dllaList.next[prev] = next;
    this->dllaList.prev[next] = prev;
    this->dllaList.size--;

    this->dllaList.next[poz.currentIndex] = this->dllaList.firstEmpty;
    this->dllaList.firstEmpty = poz.currentIndex;

    poz.currentIndex = next;

    return element;
} /// theta(1)

ListIterator SortedIteratedList::search(TComp e) {
    ListIterator iterator = this->first();
    int current = this->dllaList.head;
    while (current != -1 && this->dllaList.elements[current] != e){
        iterator.next();
        current = iterator.currentIndex;
    }
    return iterator;
} /// theta(nrNodes)

void SortedIteratedList::add(TComp e) {
    if (this->dllaList.firstEmpty == -1) { // resize if it's full
        resize(this->dllaList.capacity * 2);
    }

    // case 1: add element to empty list
    if (this->size() == 0) {
        int newPos = this->dllaList.firstEmpty;  // get new position
        this->dllaList.firstEmpty = this->dllaList.next[this->dllaList.firstEmpty];  // get the first new empty
        this->dllaList.elements[newPos] = e;  // add elem to array
        this->dllaList.next[newPos] = this->dllaList.head;
        this->dllaList.prev[newPos] = this->dllaList.tail;
        this->dllaList.head = newPos;  // modify tail and head
        this->dllaList.tail = newPos;
        this->dllaList.size++;
        return;
    }

    int current = this->dllaList.head;  // current Index

    // try to find where to add the element
    bool itIsHead = false;
    bool itIsTail = false;
    if (!this->relation(this->dllaList.elements[this->dllaList.head], e))
        itIsHead = true;
    if (this->relation(this->dllaList.elements[this->dllaList.tail], e)){
        itIsTail = true; // don't parse if it's tail.
    }else {
        while (current != -1 and this->relation(this->dllaList.elements[current], e)) {
            current = this->dllaList.next[current];
        }
    }

    // case2: add to beginning
    if (!itIsTail)
    {
        int nextPos = this->dllaList.firstEmpty; // get new position
        this->dllaList.firstEmpty = this->dllaList.next[this->dllaList.firstEmpty];  // create new first empty slot

        // move current element to new slot to make space for e
        this->dllaList.elements[nextPos] = this->dllaList.elements[current];
        this->dllaList.next[nextPos] = this->dllaList.next[current];
        this->dllaList.prev[nextPos] = current;
        if(this->dllaList.next[nextPos] == -1){ // in case we move the tail
            this->dllaList.tail = nextPos;
        }
        else{
            int next = this->dllaList.next[nextPos];
            this->dllaList.prev[next] = nextPos;
        }

        // add the element
        this->dllaList.elements[current] = e;
        this->dllaList.next[current] = nextPos;
        this->dllaList.size++;

        if (itIsHead)
            this->dllaList.head = current;}

    // case3: add to end
    if(itIsTail){
        int nextPos = this->dllaList.firstEmpty; // get new position
        int oldTail = this->dllaList.tail;
        this->dllaList.tail = nextPos;
        this->dllaList.firstEmpty = this->dllaList.next[this->dllaList.firstEmpty];  // create new first empty slot

        // add the element
        this->dllaList.elements[nextPos] = e;
        this->dllaList.next[oldTail] = nextPos;
        this->dllaList.next[nextPos] = -1;
        this->dllaList.prev[nextPos] = oldTail;
        this->dllaList.size++;
    }

} /// BC: theta(1) WC: theta(nrNodes) Total: O(nrNodes)

void SortedIteratedList::resize(int newCapacity){
    auto* newElements = new TComp[newCapacity];
    int* newNext = new int[newCapacity];
    int* newPrev = new int[newCapacity];

    for (int i=0; i<this->dllaList.capacity; i++){
        newElements[i] = this->dllaList.elements[i];
        newNext[i] = this->dllaList.next[i];
        newPrev[i] = this->dllaList.prev[i];
    }

    for (int i=this->dllaList.capacity; i<newCapacity-1; i++)
        newNext[i] = i+1;

    for (int i=this->dllaList.capacity+1; i<newCapacity; i++)
        newPrev[i] = i-1;

    newNext[newCapacity-1] = -1;
    newPrev[this->dllaList.capacity] = this->dllaList.head;

    delete[] this->dllaList.elements;
    delete[] this->dllaList.next;
    delete[] this->dllaList.prev;

    this->dllaList.elements = newElements;
    this->dllaList.next = newNext;
    this->dllaList.prev = newPrev;
    this->dllaList.firstEmpty = this->dllaList.capacity;
    this->dllaList.capacity = newCapacity;

} /// theta(capacity)

SortedIteratedList::~SortedIteratedList() {
    delete []this->dllaList.elements;
    delete []this->dllaList.next;
    delete []this->dllaList.prev;
}
///Theta(1)