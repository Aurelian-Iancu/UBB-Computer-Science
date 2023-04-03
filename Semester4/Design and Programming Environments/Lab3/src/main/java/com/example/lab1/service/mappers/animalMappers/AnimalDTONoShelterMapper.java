package com.example.lab1.service.mappers.animalMappers;

import com.example.lab1.model.Animal;
import com.example.lab1.modelDTO.animalDTO.AnimalDTONoShelter;
import org.springframework.stereotype.Service;

import java.util.function.Function;

@Service
public class AnimalDTONoShelterMapper  implements Function<Animal, AnimalDTONoShelter> {
    @Override
    public AnimalDTONoShelter apply(Animal animal) {
        return new AnimalDTONoShelter(
                animal.getAnimalId(),
                animal.getName(),
                animal.getType(),
                animal.getWeight(),
                animal.getDateOfBirth(),
                animal.getBreed()
        );
    }
}
