

#include "domain.h"
#include "repository.h"
#include "dynamicVector.h"
#include "service.h"
#include "ui.h"
#include "tests.h"
#include <cassert>


void Tests::testRemove() {
    auto v1 = new DynamicVector<Protein>(10);
    auto repo = new Repository(v1);
    repo->initialiseRepo();
    auto service = new Service(repo);

    assert(repo->getSizeRepo() == 5);
    repo->removeRepo(0);
    assert(repo->getSizeRepo() == 4);

    int removed = service->removeService("Human", "Keratin");

    assert(removed == 1);

    removed = service->removeService("Human", "Keratin");

    assert(removed == 0);
}

void Tests::testFilter() {
    auto v1 = new DynamicVector<Protein>(10);
    auto repo = new Repository(v1);
    repo->initialiseRepo();
    auto service = new Service(repo);

    auto result = new Protein[repo->getSizeRepo()];

    int filtered = service->filter("ABCDEF", result);

    assert(filtered == 3);
    assert(result[0].getName() == "Keratin");
    assert(result[1].getName() == "Keratin");
    assert(result[2].getName() == "Myosin-2");


}

