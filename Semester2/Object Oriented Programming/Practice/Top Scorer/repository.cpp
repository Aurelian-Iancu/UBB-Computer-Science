
#include "domain.h"
#include "repository.h"

#include <string>



Repository::Repository(DynamicVector<TopScorer> *repoArray) {
    this->database = repoArray;

}

void Repository::initialiseRepo()
{
    TopScorer t1 = TopScorer("Nora_Mork", "NOR", "Larvik", 83);
    TopScorer t2 = TopScorer("Isabelle_Gullden", "SWE", "CSM_Bucurest", 80);
    TopScorer t3 = TopScorer("Cristina_Neagu", "ROW", "Buducnost", 63);
    TopScorer t4 = TopScorer("Allison_Pineau", "FRA", "HCM_Baia_Mare", 82);
    TopScorer t5 = TopScorer("Ilina_Ecaterina", "RUS", "Rostov_Don", 80);
    this->database->addVector(t1);
    this->database->addVector(t2);
    this->database->addVector(t3);
    this->database->addVector(t4);
    this->database->addVector(t5);


}

void Repository::addRepo(TopScorer &topScorer) {
    this->database->addVector(topScorer);
}

