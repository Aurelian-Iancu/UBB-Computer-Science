#include "ui.h"
#include "repository.h"
#include <crtdbg.h>
#include <stdio.h>
#include <stdlib.h>

void tests()
{
    testProduct();
    testVector();
    testRepo();
    testService();
    printf("All tests passed successfully!! <3\n");
}

int main()
{
    Repo* repo = createRepo();
    Service* service = createService(repo);

    addService(service, "chicken", "meat", 20, 2002);
    addService(service, "chicken1", "meat", 15, 2022);
    addService(service, "beef", "meat", 13, 2014);
    addService(service, "chocolate", "sweets", 62, 2016);
    addService(service, "pork", "meat", 40, 2015);
    addService(service, "turkey", "meat", 21, 2020);
    addService(service, "apple", "fruit", 50, 2022);

    addService(service, "banana", "fruit", 73, 2011);
    addService(service, "milk", "dairy", 84, 2017);
    addService(service, "cheese", "dairy", 95, 2018);

    UI* ui = createUI(service);

    tests();

    start(ui);

    destroyUI(ui);
    printf("%d", _CrtDumpMemoryLeaks());

    return 0;
}


