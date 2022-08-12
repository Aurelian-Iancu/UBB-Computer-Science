#include "tests.h"
#include "dynamicVector.h"
#include "repository.h"
#include "service.h"
#include "cassert"

void Tests::testAdd() {
    auto* v1 = new DynamicVector<TopScorer>(10);
    auto* repo = new Repository(v1);
    auto* service = new Service(repo);

    assert(repo->getSizeRepo() == 0);
    TopScorer t1 = TopScorer("Nora_Mork", "NOR", "Larvik", 83);
    repo->addRepo(t1);
    assert(repo->getSizeRepo() == 1);

    TopScorer t2 = TopScorer("Isabelle_Gullden", "SWE", "CSM_Bucurest", 80);
    repo->addRepo(t2);
    assert(repo->getSizeRepo() == 2);

    int added = service->addService("Isabelle_Gullden", "mata", "mata", 11);
    assert(added == 1);
    added = service->addService("mata", "mata", "mata", 11);
    assert(added == 0);


}

void Tests::testFilter() {
    auto* v1 = new DynamicVector<TopScorer>(10);
    auto* repo = new Repository(v1);
    auto* service = new Service(repo);

    TopScorer t1 = TopScorer("Nora_Mork", "NOR", "Larvik", 83);
    TopScorer t2 = TopScorer("Isabelle_Gullden", "SWE", "CSM_Bucurest", 80);
    TopScorer t3 = TopScorer("Cristina_Neagu", "ROW", "Buducnost", 63);
    TopScorer t4 = TopScorer("Allison_Pineau", "FRA", "HCM_Baia_Mare", 82);
    TopScorer t5 = TopScorer("Ilina_Ecaterina", "RUS", "Rostov_Don", 80);

    repo->addRepo(t1);
    repo->addRepo(t2);
    repo->addRepo(t3);
    repo->addRepo(t4);
    repo->addRepo(t5);

    TopScorer t6 = TopScorer("dasfsa", "NOR", "Larvik", 98);
    TopScorer t7 = TopScorer("fdsafsa", "NOR", "Larvik", 111);

    repo->addRepo(t6);
    repo->addRepo(t7);

    auto result = new TopScorer[service->getSizeService()];

    int filtered = service->filter("Larvik", result);

    assert(filtered == 3);
    assert(result[0].getNumberOfGoals() == 111);
    assert(result[1].getNumberOfGoals() == 98);
    assert(result[2].getNumberOfGoals() == 83);

}
