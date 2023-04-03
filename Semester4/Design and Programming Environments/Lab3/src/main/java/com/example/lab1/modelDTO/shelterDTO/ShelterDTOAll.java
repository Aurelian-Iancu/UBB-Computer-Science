package com.example.lab1.modelDTO.shelterDTO;

public record ShelterDTOAll (
        Long shelterId,
        String name,
        String address,
        Integer numberOfVolunteers,
        Integer capacity,
        String city
){
}
