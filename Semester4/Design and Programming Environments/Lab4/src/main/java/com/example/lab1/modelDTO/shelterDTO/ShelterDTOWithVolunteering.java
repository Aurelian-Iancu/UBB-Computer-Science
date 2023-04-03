package com.example.lab1.modelDTO.shelterDTO;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ShelterDTOWithVolunteering{
        Long shelterId;
        String name;
        String address;
        Integer numberOfVolunteers;
        Integer capacity;
        String city;
        Integer hoursPerWeek;
        String role;
}
