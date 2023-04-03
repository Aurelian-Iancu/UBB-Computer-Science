package com.example.lab1.modelDTO.shelterDTO;

import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.animalDTO.AnimalDTONoShelter;

import java.util.List;

public record ShelterDTOById (
        Long shelterId,
        String name,
        String address,
        Integer numberOfVolunteers,
        Integer capacity,
        String city,
        List<AnimalDTONoShelter> animals
) {
}
