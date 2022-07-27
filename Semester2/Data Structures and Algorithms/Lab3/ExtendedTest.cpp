#include "ExtendedTest.h"
#include <assert.h>
#include <cstdlib>
#include <vector>
#include <iostream>
#include "ListIterator.h"
#include "SortedIteratedList.h"

using namespace std;


//relation order - ascending
bool asc(TComp c1, TComp c2) {
	if (c1 <= c2) {
		return true;
	} else {
		return false;
	}
}

//relation order - descending
bool desc(TComp c1, TComp c2) {
	if (c1 >= c2) {
		return true;
	} else {
		return false;
	}
}

void testIteratorSteps(SortedIteratedList& sil, Relation r) {
	ListIterator li = sil.first();
	TComp elem = li.getCurrent();
	int count = 0;
	if (li.valid()) {
		count++;
		li.next();
	}
	while (li.valid()) {
		TComp elem2 = li.getCurrent();
		assert(r(elem, elem2));
		elem = elem2;
		count++;
		li.next();
	}
	assert(count == sil.size());
}

void testCreate() {
	cout << "Test create" << endl;
	SortedIteratedList list = SortedIteratedList(asc);
	assert(list.size() == 0);
	assert(list.isEmpty());

	ListIterator it = list.first();
	assert(!it.valid());
	it.first();

	for (int i = 0; i < 10; i++) {
		assert(!it.valid());
		assert(!list.search(i).valid());
		try {
			assert(list.getElement(it));
			assert(false);
		} catch (exception&) {
			assert(true);
		}
		try {
			assert(list.remove(it));
			assert(false);
		} catch (exception&) {
			assert(true);
		}
		try {
			it.next();
			assert(false);
		} catch(exception& ex) {
			assert(true);
		}
	}
}

//generate a vector with values between cMin and cMax so that
//1) no value that is >=cMin and <=cMax which is a multiple of s is not included
//2) values v, v>=cMin and v<=cMax which are a multiple of m (but not of s) are included c/m + 1 times
//3) values >=cMin and <=cMax are in random order
vector<int> random(int cMin, int cMax, int s, int m) {
	vector<int> v;
	for (int c = cMin; c <= cMax; c++) {
		if (c % s != 0) {
			v.push_back(c);
			if (c % m == 0) {
				for (int j = 0; j < c / m; j++) {
					v.push_back(c);
				}
			}
		}
	}
	int n = v.size();
	for (int i = 0; i < n - 1; i++) {
		int j = i + rand() % (n - i);
		swap(v[i], v[j]);
	}
	return v;
}

//generate a vector containing values >=cMin and <=cMax, each included one time, in random order
vector<int> random(int cMin, int cMax) {
	vector<int> v;
	for (int c = cMin; c <= cMax; c++) {
		v.push_back(c);
	}

	int n = v.size();
	for (int i = 0; i < n - 1; i++) {
		int j = i + rand() % (n - i);
		swap(v[i], v[j]);
	}
	return v;
}

//populate the sorted list with values >=cMin and <=cMax a.i.:
//1) no value that is >=cMin and <=cMax which is a multiple of s is not included
//2) values v, v>=cMin and v<=cMax which are a multiple of m (but not of s) are included c/m + 1 times
//3) values >=cMin and <=cMax are in random order
int populate(SortedIteratedList& list, int cMin, int cMax, int s, int m) {
	vector<int> v = random(cMin, cMax, s, m);
	int n = v.size();
	for (int i = 0; i < n; i++) {
		list.add(v[i]);
	}
	return n;
}

//populate the sorted list with values >=cMin and <=cMax, each included one time, in random order
void populate(SortedIteratedList& list, int cMin, int cMax) {
	vector<int> v = random(cMin, cMax);
	int n = v.size();
	for (int i = 0; i < n; i++) {
		list.add(v[i]);
	}
}

void testAddAndSearch(Relation r) {
	cout << "Test add and search" << endl;
	SortedIteratedList list = SortedIteratedList(r);
	int vMin = 10;
	int vMax = 30;
	int s = 5;
	int m = 3;
	int n = populate(list, vMin, vMax, s, m);
	assert(!list.isEmpty());
	testIteratorSteps(list, r);
	assert(list.size() == n);

	//we can't find values outside the interval or on invalid positions
	int d = 30;
	for (int i = 1; i <= d; i++) {
		assert(!list.search(vMin - i).valid());
		assert(!list.search(vMax + i).valid());
	}

	//check the relation order
	ListIterator it = list.first();
	assert(it.valid());
	TComp prev = it.getCurrent();
	it.next();
	while (it.valid()) {
		TComp current = list.getElement(it);
		assert(r(prev, current));
		prev = current;
		it.next();
	}

	//check if added values can be found
		for (int v = vMin; v <= vMax; v++) {
			testIteratorSteps(list, r);
			ListIterator p = list.search(v);
			//we can't find values which are a multiple of s
			assert(p.valid() == (v % s != 0));
			//values which are a multiple of m can be found exactly v/m+1 times
			if (p.valid() && v%m == 0){
            	for (int i=0; i<=v/m; i++){
            		try{
            			assert(list.remove(p) == v);
            		} catch (exception&) {
						assert(false);
					}
            	}
            	assert(!list.search(v).valid());
            }
		}



}

void testDeleteSearch(Relation r) {
	cout << "Test delete and search" << endl;
	SortedIteratedList list = SortedIteratedList(r);
	int vMin = 0;
	int vMax = 100;
	populate(list, vMin, vMax);
	testIteratorSteps(list, r);
	int d = 30;
	for (int i = 1; i <= d; i++) {
		try {
			ListIterator li = list.search(vMax + 1);
			list.remove(li);
			assert(false);
		} catch (exception&) {
			assert(true);
		}
		testIteratorSteps(list, r);
	}

	assert(!list.isEmpty());
	assert(list.size() == vMax - vMin + 1);
	ListIterator it1 = list.first();
	assert(it1.valid());
	TComp deleted = NULL_TCOMP;
	try {
		deleted = list.remove(it1);
		assert(list.size() == vMax - vMin);
		TComp newFirst = it1.getCurrent();
		assert(newFirst != deleted);
		assert(r(deleted, newFirst));
		it1.first();
		ListIterator it2 = list.first();
		assert(it1.getCurrent() == newFirst && it2.getCurrent() == newFirst);
	} catch (exception&) {
		assert(false);
	}

	//delete values in random order while checking the relation order
	vector<int> vs = random(vMin, vMax);
	int n = vs.size();
	for (int i = 0; i < n; i++) {
		int v = vs[i];
		try {
			ListIterator it1  = list.search(v);
			TComp deleteCurrent = list.remove(it1);
			assert(deleteCurrent != deleted);
			assert(deleteCurrent == v);
			assert(!list.search(v).valid());

			if (!list.isEmpty()) {
				assert(list.first().valid());
				ListIterator it2 = list.first();
				assert(it2.valid());
				TComp prev = it2.getCurrent();
				while (it2.valid()) {
					TComp current = list.getElement(it2);
					assert(r(prev, current));
					assert(!r(deleteCurrent, current) || !r(current, deleteCurrent));
					prev = current;
					it2.next();
				}
			}

		} catch (exception&) {
			assert(v == deleted);
		}
	}

	assert(list.isEmpty());
	assert(list.size() == 0);
}

void testDeleteSearch() {
	testDeleteSearch(asc);
	testDeleteSearch(desc);
}

void testAddAndSearch() {
	testAddAndSearch(asc);
	testAddAndSearch(desc);
}


void testQuantity(){
	cout << "Test quantity" << endl;
	SortedIteratedList list = SortedIteratedList(asc);

	int vMin = 3000;
	int vMax = 6000;
	vector<int> values  = random(vMin, vMax);
	int n = values.size();
    for (int i = 0; i < n; i++){
    	list.add(values[i]);
    }

    assert(list.size() == vMax - vMin + 1);
    for (int v = vMin; v <= vMax; v++){
      	assert(list.search(v).valid());
      	assert(list.search(v).getCurrent() == v);
    }

    ListIterator it  = list.first();
    assert(it.valid());
    TComp firstElem = it.getCurrent();
    it.first();
    assert(it.valid());
    assert(it.getCurrent() == firstElem);
    for (int i = 0; i < list.size(); i++) {
    	it.next();
    }

    assert(!it.valid());
    it.first();
    while (it.valid()){
        TComp v  = it.getCurrent();
        assert(vMin <= v && v<=vMax);
        it.next();
    }
    assert(!it.valid());


    int d = 100;
	//consider the interval [vMin-d, vMax+d]
	for (int v = vMin-d; v <= vMax+d; v++){
		//check that only values from the interval [vMin, vMax] are included in the list
		assert(list.search(v).valid() == (vMin <= v && v <= vMax));
    	 try{
			 ListIterator li = list.search(v);
    		 assert(list.remove(li));
    		 assert(vMin <= v && v <= vMax);
    	 } catch (exception&) {
			 assert(vMin > v || v > vMax);
		}
    }
    assert(list.size() == 0);
    assert(list.isEmpty());
}

void testAllExtended() {
	testCreate();
	testAddAndSearch();
	testDeleteSearch();
    testQuantity();
}

