package Controller;

import Model.Animal;
import Model.Birds;
import Model.Cows;
import Model.Pigs;
import Repository.InterfaceRepository;

import java.util.Objects;

public class Controller {
    private InterfaceRepository repository;

    public Controller(InterfaceRepository repository) {
        this.repository = repository;
    }

    public void add(String type, float weight) {
        if (Objects.equals(type, "bird")) {
            Birds bird = new Birds(weight);
            this.repository.add(bird);
        } else if (Objects.equals(type, "cow")) {
            Cows cow = new Cows(weight);
            this.repository.add(cow);
        } else if (Objects.equals(type, "pig")) {
            Pigs pig = new Pigs(weight);
            this.repository.add(pig);
        }

    }

    public void remove(int index) {
        this.repository.remove(index);
    }

    public Animal[] getAllController() {
        return this.repository.getAllRepo();
    }


    public int getSizeController() {
        return this.repository.getSizeRepo();
    }

    public Animal[] getFiltered(float weight) {
        Animal[] copy = new Animal[this.repository.getSizeRepo()];
        int size = 0;
        for (Animal animal : this.repository.getAllRepo())
            if (animal != null)
                if (animal.getWeight() > weight)
                    copy[size++] = animal;
        Animal[] toReturn = new Animal[size];
        System.arraycopy(copy, 0, toReturn, 0, size);
        return toReturn;
    }
}
