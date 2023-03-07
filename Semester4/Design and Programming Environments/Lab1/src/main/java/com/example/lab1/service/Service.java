package com.example.lab1.service;

import com.example.lab1.model.Dog;
import com.example.lab1.repository.Repository;
import java.util.List;

@org.springframework.stereotype.Service
public class Service {
    private final Repository repository;

    public Service(Repository repository) {
        this.repository = repository;
    }

    public List<Dog> getDogsService(){
        return repository.getDogListRepo();
    }

    public Dog addDogService(Dog dog){
        return this.repository.addDogRepo(dog);
    }

    public String removeDogService(int id){
        this.repository.removeDogRepo(id);
        return "dog removed !!" + id;
    }

    public Dog updateDogService(int id, Dog dog){
        this.repository.updateDogRepo(id, dog);
        return dog;
    }


}
