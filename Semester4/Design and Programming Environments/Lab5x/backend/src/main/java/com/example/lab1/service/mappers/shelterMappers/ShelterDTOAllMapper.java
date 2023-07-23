package com.example.lab1.service.mappers.shelterMappers;

import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAll;
import org.springframework.stereotype.Service;

import java.util.function.Function;
@Service
public class ShelterDTOAllMapper implements Function<Shelter, ShelterDTOAll> {
    @Override
    public ShelterDTOAll apply(Shelter shelter) {
        return new ShelterDTOAll(
                shelter.getShelterId(),
                shelter.getName(),
                shelter.getAddress(),
                shelter.getNumberOfVolunteers(),
                shelter.getCapacity(),
                shelter.getCity(),
                shelter.getDescription()
        );
    }
}
