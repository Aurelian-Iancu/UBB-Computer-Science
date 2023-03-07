package com.example.lab1.controller;

import com.example.lab1.model.Dog;
import com.example.lab1.service.Service;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class Controller {
    private final Service service;


    public Controller(Service service) {
        this.service = service;
    }

    @PostMapping("/addDog")
    public Dog addDog(@RequestBody Dog dog){
        return service.addDogService(dog);
    }

    @GetMapping("/getDogs")
    public List<Dog> getAllDogs(){
        return service.getDogsService();
    }

    @PutMapping("/updateDog/{id}")
    public Dog updateDog(@PathVariable int id, @RequestBody Dog dog){
        return service.updateDogService(id, dog);
    }

    @DeleteMapping("/deleteDog/{id}")
    public String deleteDog(@PathVariable int id){
        return service.removeDogService(id);
    }
}
