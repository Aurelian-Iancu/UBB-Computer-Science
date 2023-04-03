package com.example.lab1.repository;

import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;

import java.util.List;

public interface ShelterRepositoryCustom {
    List<ShelterDTOCount> findSheltersOrderedByNumberOfAnimalsAsc();

    List<ShelterDTOAverage> findSheltersOrderedByAverageWeightDesc();
}
