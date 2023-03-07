package com.example.lab1.repository;

import com.example.lab1.model.Dog;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@org.springframework.stereotype.Repository
public class Repository {
    private List<Dog> dogList;

    @Autowired
    public Repository(){
        dogList = new ArrayList<>();

        Dog dog1 = new Dog(1, "Dog1", 15, 10, "Labrador", "dry food");
        Dog dog2 = new Dog(2, "Dog1", 15, 10, "Labrador", "dry food");
        Dog dog3 = new Dog(3, "Dog1", 15, 10, "Labrador", "dry food");
        Dog dog4 = new Dog(4, "Dog1", 15, 10, "Labrador", "dry food");
        Dog dog5 = new Dog(5, "Dog1", 15, 10, "Labrador", "dry food");

        dogList.addAll(Arrays.asList(dog1, dog2, dog3, dog4, dog5));
    }

    public List<Dog> getDogListRepo(){
        return this.dogList;
    }

    public Dog addDogRepo(Dog dog){
        this.dogList.add(dog);
        return dog;
    }

    public void removeDogRepo(int id){
        Dog dog = new Dog();
        for(Dog loopDog: this.dogList){
            if(loopDog.getDogId() == id){
                dog = loopDog;
            }
        }
        this.dogList.remove(dog);
    }

    public void updateDogRepo(int id, Dog newDog)
    {
        int foundIndex = -1;
        for(int i = 0; i < this.dogList.size(); i++)
        {
            if(this.dogList.get(i).getDogId() == id){
                foundIndex = i;
            }
        }
        this.dogList.set(foundIndex, newDog);
    }
}
