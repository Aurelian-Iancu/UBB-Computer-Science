package com.example.lab1.modelDTO.animalDTO;

import java.time.LocalDate;

public record AnimalDTONoShelter(
        Long animalId,
        String name,
        String type,
        Double weight,
        LocalDate dateOfBirth,
        String breed
){

}
