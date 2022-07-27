#include <assert.h>

#include "SortedIteratedList.h"
#include "ListIterator.h"
#include <iostream>

#include <exception>
using namespace std;

bool relation1(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

void testAll(){
	SortedIteratedList list = SortedIteratedList(relation1);
	assert(list.size() == 0);
	assert(list.isEmpty());
    list.add(1);
    assert(list.size() == 1);
    assert(!list.isEmpty());
    ListIterator it = list.search(1);
    assert(it.valid());
    assert(it.getCurrent() == 1);
    it.next();
    assert(!it.valid());
    it.first();
    assert(it.valid());
    ListIterator itFirst = list.first();
    assert(itFirst.valid());
    assert(itFirst.getCurrent() == 1);
    assert(list.remove(it) == 1);
    assert(list.size() == 0);
    assert(list.isEmpty());
}

void testExtra()
{
    SortedIteratedList list = SortedIteratedList(relation1);
    assert(list.size() == 0);
    assert(list.isEmpty());
    list.add(1);
    list.add(2);
    list.add(15);
    list.add(10);
    assert(list.size() == 4);
    ListIterator it = list.first();

    assert(it.remove() == 1);
    assert(list.size() == 3);

    assert(it.remove() == 2);
    assert(it.remove() == 10);
    assert(list.size() == 1);



    std::cout << "EXTRA" << endl;

}

