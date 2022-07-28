
#include "tests.h"

#include "dynamicVector.h"
#include "repository.h"
#include "service.h"
#include "domain.h"
#include <assert.h>


void Tests::testsAdd() {

    auto v1 = new DynamicVector<Task>(10);
    auto repo = new Repository(v1);
    auto service = new Service(repo);

    repo->initialiseRepo();

    assert(repo->getSizeRepo() == 5);
    Task t1 = Task("Solve_OOP_assignment", 120, 1);

    repo->addRepo(t1);
    assert(repo->getSizeRepo() == 6);

    int added = service->addService("idk", 3, 3);

    assert(added == 0);

    added = service->addService("idk", 3, 3);

    assert(added == 1);


}

void Tests::testFilter() {
    auto v1 = new DynamicVector<Task>(10);
    auto repo = new Repository(v1);
    auto service = new Service(repo);

    repo->initialiseRepo();

    auto result = new Task[service->getSizeService()];
    int filtered = service->filtered(3, result);

    assert(filtered == 4);

    assert(result[0].getDuration() == 240);
    assert(result[1].getDuration() == 120);
    assert(result[2].getDuration() == 120);
    assert(result[3].getDuration() == 45);

}
