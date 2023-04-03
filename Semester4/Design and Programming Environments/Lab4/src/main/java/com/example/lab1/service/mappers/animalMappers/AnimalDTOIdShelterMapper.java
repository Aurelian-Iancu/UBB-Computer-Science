package com.example.lab1.service.mappers.animalMappers;

import com.example.lab1.model.Animal;
import com.example.lab1.modelDTO.animalDTO.AnimalDTOIdShelter;
import org.springframework.stereotype.Service;

import java.util.function.Function;

@Service
public class AnimalDTOIdShelterMapper implements Function<Animal, AnimalDTOIdShelter> {
    @Override
    public AnimalDTOIdShelter apply(Animal animal){
        return new AnimalDTOIdShelter(
                animal.getAnimalId(),
                animal.getName(),
                animal.getType(),
                animal.getWeight(),
                animal.getDateOfBirth(),
                animal.getBreed(),
                animal.getShelter().getShelterId()
        );
    }
}
