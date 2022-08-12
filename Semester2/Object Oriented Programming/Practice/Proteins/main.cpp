#include <iostream>

#include "domain.h"
#include "repository.h"
#include "dynamicVector.h"
#include "service.h"
#include "ui.h"
#include "tests.h"

#include <iostream>

using namespace std;

void tests()
{
    Tests t;
    t.testFilter();
    t.testRemove();
    cout <<"Tests passed" << endl;
}
int main() {
    auto v1 = new DynamicVector<Protein>(10);
    auto repo = new Repository(v1);
    repo->initialiseRepo();
    auto service = new Service(repo);

    auto ui = new UI(service);

    tests();

    ui->start();
}
