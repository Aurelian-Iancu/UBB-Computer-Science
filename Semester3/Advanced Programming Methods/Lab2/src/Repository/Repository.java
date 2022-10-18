package Repository;

import Model.Animal;

public class Repository implements InterfaceRepository{
    private Animal[] animals;
    private int numberOfAnimals;

    public Repository(int numberOfAnimals) {
        this.animals = new Animal[numberOfAnimals];
        this.numberOfAnimals = 0;
    }

    @Override
    public void add(Animal animal) {
        this.animals[numberOfAnimals] = animal;
        this.numberOfAnimals++;
    }

    @Override
    public void remove(int index) {
        Animal[] animalCopy = new Animal[this.numberOfAnimals - 1];
        int j = 0;
        for (int i = 0; i < this.numberOfAnimals; i++) {
            if (i != index) {
                animalCopy[j] = this.animals[i];
                j++;
            }
        }
        this.animals = animalCopy;
        this.numberOfAnimals--;
    }

    @Override
    public Animal[] getAllRepo() {
        return this.animals;
    }

    @Override
    public int getSizeRepo() {
        return this.numberOfAnimals;
    }
}
