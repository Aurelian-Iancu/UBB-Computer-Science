package com.example.lab1.service;

import com.example.lab1.exceptions.ShelterNotFoundException;
import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAll;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOById;

import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;
import com.example.lab1.repository.ShelterRepository;
import com.example.lab1.repository.ShelterRepositoryCustom;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOAllMapper;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOByIdMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class ShelterService {
    private final ShelterRepository shelterRepository;
    private final ShelterDTOByIdMapper shelterDTOByIdMapper;
    private final ShelterDTOAllMapper shelterDTOAllMapper;
    private final ShelterRepositoryCustom shelterRepositoryCustom;

    @Autowired
    public ShelterService(ShelterRepository shelterRepository,
                          ShelterDTOByIdMapper shelterDTOByIdMapper,
                          ShelterDTOAllMapper shelterDTOAllMapper, ShelterRepositoryCustom shelterRepositoryCustom) {
        this.shelterRepository = shelterRepository;
        this.shelterDTOByIdMapper = shelterDTOByIdMapper;
        this.shelterDTOAllMapper = shelterDTOAllMapper;
        this.shelterRepositoryCustom = shelterRepositoryCustom;
    }

    public List<ShelterDTOAll> findAllShelters(){
        return shelterRepository.findAll()
                .stream()
                .map(shelterDTOAllMapper)
                .collect(Collectors.toList());
    }
    public Optional<ShelterDTOById> findShelterById(Long id){
        List<ShelterDTOById> collect = shelterRepository.findById(id)
                .stream()
                .map(shelterDTOByIdMapper)
                .toList();

        return collect.stream().findFirst();
    }

    public Shelter saveShelter(Shelter shelter){
        return this.shelterRepository.save(shelter);
    }

    public Shelter updateShelter(Shelter shelter, Long id){
        Shelter oldShelter = shelterRepository.findById(id).orElseThrow(() -> new ShelterNotFoundException(id));
        if(oldShelter != null){
            oldShelter.setName(shelter.getName());
            oldShelter.setAddress(shelter.getAddress());
            oldShelter.setNumberOfVolunteers(shelter.getNumberOfVolunteers());
            oldShelter.setCapacity(shelter.getCapacity());
            oldShelter.setCity(shelter.getCity());
            shelterRepository.save(oldShelter);
            return oldShelter;
        }

        return shelterRepository.save(shelter);

    }

    public void deleteShelter(Long id){
        this.shelterRepository.deleteById(id);
    }

    public List<ShelterDTOCount> getSheltersOrderedByNumberOfAnimalsAsc(){
        return this.shelterRepositoryCustom.findSheltersOrderedByNumberOfAnimalsAsc();
    }

    public List<ShelterDTOAverage> getSheltersOrderedByAverageWeightDesc() {
        return this.shelterRepositoryCustom.findSheltersOrderedByAverageWeightDesc();
    }
}
