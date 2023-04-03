package com.example.lab1.service.mappers.shelterMappers;

import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOById;
import com.example.lab1.service.mappers.animalMappers.AnimalDTONoShelterMapper;
import org.springframework.stereotype.Service;

import java.util.function.Function;
import java.util.stream.Collectors;

@Service
public class ShelterDTOByIdMapper implements Function<Shelter, ShelterDTOById> {

    private static final AnimalDTONoShelterMapper animalDTONoShelterMapper = new AnimalDTONoShelterMapper();

    @Override
    public ShelterDTOById apply(Shelter shelter) {
        return new ShelterDTOById(
                shelter.getShelterId(),
                shelter.getName(),
                shelter.getAddress(),
                shelter.getNumberOfVolunteers(),
                shelter.getCapacity(),
                shelter.getCity(),
                shelter.getAnimals()
                        .stream()
                        .map(animalDTONoShelterMapper)
                        .collect(Collectors.toList())
        );
    }
}
