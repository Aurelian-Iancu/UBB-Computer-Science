package com.example.lab1.controller;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.animalDTO.AnimalDTOIdShelter;
import com.example.lab1.service.AnimalService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/animal")
public class AnimalController {
    private final AnimalService animalService;

    public AnimalController(AnimalService animalService) {
        this.animalService = animalService;
    }

    //get all animals only with the id of their shelter
    @GetMapping("/getAll")
    public List<AnimalDTOIdShelter> findAllAnimals(){
        return animalService.findAllAnimals();
    }

    //get animal by id with all the info about its shelter
    @GetMapping("/getById/{id}")
    public Optional<Animal> findAnimalById(@PathVariable("id") Long id){
        return animalService.findAnimalById(id);
    }

    //Add an animal in existent shelter
    @PostMapping("/save/shelter{id}")
    public Animal saveAnimal(@RequestBody Animal animal, @PathVariable("id") Long id){
        return animalService.saveAnimal(animal, id);
    }

    //update animal with id = id
    @PutMapping("/update/{id}")
    public Animal updateAnimal(@RequestBody Animal animal, @PathVariable("id") Long id){
        return animalService.updateAnimal(animal, id);
    }

    @PutMapping("/update/animal{animalId}/shelter{shelterId}")
    public Shelter updateShelter(@PathVariable Long animalId, @PathVariable Long shelterId){
        return animalService.updateShelter(animalId, shelterId);
    }

    //delete animal with id = id
    @DeleteMapping("/delete/{id}")
    public void deleteAnimal(@PathVariable("id") Long id){
        animalService.deleteAnimal(id);
    }

    //get only the animals with the weight greater than a give one
    @GetMapping("/filter/{weight}")
    public Object filterAnimals(@PathVariable("weight") Double weight){
        if(weight == null){
            return this.animalService.findAllAnimals();
        }
        return animalService.findByWeightGreaterThan(weight);
    }
}
