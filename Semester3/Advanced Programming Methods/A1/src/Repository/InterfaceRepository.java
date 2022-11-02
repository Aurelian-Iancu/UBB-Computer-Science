package Repository;

import Model.Animal;

public interface InterfaceRepository {
    void add(Animal animal);
    void remove(int index);
    Animal[] getAllRepo();
    int getSizeRepo();
}
