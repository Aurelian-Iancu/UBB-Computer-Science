#include "observer.h"
#include <algorithm>

void Subject::addObserver(Observer* o)
{
    observers.push_back(o);
}

void Subject::removeObserver(Observer* o)
{
    auto it = find(observers.begin(), observers.end(), o);

    if (it != observers.end())
        observers.erase(it);
}

void Subject::notify()
{
    for (auto o : observers)
        o->update();
}

