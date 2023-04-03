package com.example.lab1.modelDTO.animalDTO;

public record AnimalDTOIdShelter(
        Long animalId,
        String name,
        String type,
        Double weight,
        String dateOfBirth,
        String breed,
        Long shelterId
){
}
