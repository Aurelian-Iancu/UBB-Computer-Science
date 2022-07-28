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
    t.testsAdd();
    t.testFilter();
    cout << "Tests passed!";
}
int main() {

    auto v1 = new DynamicVector<Task>(10);
    auto repo = new Repository(v1);
    auto service = new Service(repo);
    repo->initialiseRepo();

    auto ui = new UI(service);

    tests();

    ui->start();

}
