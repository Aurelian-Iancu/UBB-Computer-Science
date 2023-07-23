package com.example.lab1.controller;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.animalDTO.AnimalDTOIdShelter;
import com.example.lab1.service.AnimalService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping("/api/animal")
@Validated
public class AnimalController {
    private final AnimalService animalService;

    public AnimalController(AnimalService animalService) {
        this.animalService = animalService;
    }

    //get all animals only with the id of their shelter
    @GetMapping("/getAll")
    ResponseEntity<List<AnimalDTOIdShelter>> findAllAnimals(@RequestParam(required = false) Double minWeight,
                                                            @RequestParam(defaultValue = "0") Integer pageNo,
                                                            @RequestParam(defaultValue = "10") Integer pageSize){
        if(minWeight == null){
            return ResponseEntity
                    .status(HttpStatus.OK)
                    .body(this.animalService.findAllAnimals(pageNo, pageSize));
        }
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.animalService.findByWeightGreaterThan(minWeight, pageNo, pageSize));
    }

    //get animal by id with all the info about its shelter
    @GetMapping("/{id}")
    ResponseEntity<Animal> findAnimalById(@PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.animalService.findAnimalById(id));
    }

    //Add an animal in existent shelter
    @PostMapping("/save/shelter{id}")
    ResponseEntity<Animal> saveAnimal(@Valid @RequestBody Animal animal, @PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(animalService.saveAnimal(animal, id));
    }

    //Add bulk animal in existent shelter
    @PostMapping("/multipleSave/shelter{id}")
    ResponseEntity<HttpStatus> saveAnimals(@RequestBody List<Animal> animals, @PathVariable("id") Long id){
        for(Animal animal : animals){
            animalService.saveAnimal(animal, id);
        }
        return ResponseEntity.accepted().body(HttpStatus.OK);
    }

    //update animal with id = id
    @PutMapping("/update/{id}")
    ResponseEntity<Animal> updateAnimal(@Valid @RequestBody Animal animal, @PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.animalService.updateAnimal(animal, id));
    }

    //delete animal with id = id
    @DeleteMapping("/delete/{id}")
    ResponseEntity<HttpStatus> deleteAnimal(@PathVariable("id") Long id){
        animalService.deleteAnimal(id);
        return ResponseEntity.accepted().body(HttpStatus.OK);
    }

//    //get only the animals with the weight greater than a give one
//    @GetMapping("/filter/{weight}")
//    public Object filterAnimals(@PathVariable("weight") Double weight){
//        if(weight == null){
//            return this.animalService.findAllAnimals();
//        }
//        return animalService.findByWeightGreaterThan(weight);
//    }
}
