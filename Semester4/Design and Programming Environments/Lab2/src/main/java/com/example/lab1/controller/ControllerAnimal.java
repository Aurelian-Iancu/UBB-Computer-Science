package com.example.lab1.controller;

import com.example.lab1.model.EntityAnimal;
import com.example.lab1.service.ServiceAnimal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/animal")
public class ControllerAnimal {
    private final ServiceAnimal serviceAnimal;

    public ControllerAnimal(ServiceAnimal serviceAnimal) {
        this.serviceAnimal = serviceAnimal;
    }

    @PostMapping("/save")
    public EntityAnimal saveAnimal(@RequestBody EntityAnimal entityAnimal){
        return serviceAnimal.saveAnimal(entityAnimal);
    }

    @GetMapping("/getAll")
    public List<EntityAnimal> findAllAnimals(){
        return serviceAnimal.findAllAnimals();
    }

    @GetMapping("/getById/{id}")
    public Optional<EntityAnimal> findAnimalById(@PathVariable("id") Long id){
        return serviceAnimal.findById(id);
    }

    @PutMapping("/update/{id}")
    public EntityAnimal updateAnimal(@RequestBody EntityAnimal entityAnimal,@PathVariable("id") Long id){
        return serviceAnimal.updateAnimal(entityAnimal, id);
    }

    @DeleteMapping("/delete/{id}")
    public void deleteAnimal(@PathVariable("id") Long id){
        serviceAnimal.deleteAnimal(id);
    }

}
