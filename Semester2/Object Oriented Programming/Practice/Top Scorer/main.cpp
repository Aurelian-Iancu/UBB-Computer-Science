#include <iostream>
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
    t.testAdd();
    t.testFilter();
    cout << "The tests passed successfully!";
}

int main() {
    auto * dynamicVector = new DynamicVector<TopScorer>(10);
    auto * repo = new Repository(dynamicVector);
    repo->initialiseRepo();
    auto * service = new Service(repo);
    auto * ui = new UI(service);

    tests();

    ui->start();

    return 0;
}
