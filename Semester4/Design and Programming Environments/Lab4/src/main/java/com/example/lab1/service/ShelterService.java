package com.example.lab1.service;

import com.example.lab1.exceptions.ShelterNotFoundException;

import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAll;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOById;

import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;
import com.example.lab1.repository.ShelterRepository;
import com.example.lab1.repository.ShelterRepositoryCustom;
import com.example.lab1.repository.VolunteerRepository;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOAllMapper;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOByIdMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ShelterService {
    private final ShelterRepository shelterRepository;
    private final ShelterDTOByIdMapper shelterDTOByIdMapper;
    private final ShelterDTOAllMapper shelterDTOAllMapper;
    private final ShelterRepositoryCustom shelterRepositoryCustom;

    private final VolunteerRepository volunteerRepository;

    @Autowired
    public ShelterService(ShelterRepository shelterRepository,
                          ShelterDTOByIdMapper shelterDTOByIdMapper,
                          ShelterDTOAllMapper shelterDTOAllMapper, ShelterRepositoryCustom shelterRepositoryCustom,
                          VolunteerRepository volunteerRepository) {
        this.shelterRepository = shelterRepository;
        this.shelterDTOByIdMapper = shelterDTOByIdMapper;
        this.shelterDTOAllMapper = shelterDTOAllMapper;
        this.shelterRepositoryCustom = shelterRepositoryCustom;
        this.volunteerRepository = volunteerRepository;
    }

    public List<ShelterDTOAll> findAllShelters(){
        return shelterRepository.findAll()
                .stream()
                .map(shelterDTOAllMapper)
                .collect(Collectors.toList());
    }

    public ShelterDTOById findShelterById(Long id){
        //return this.shelterRepository.findById(id).orElseThrow(() -> new ShelterNotFoundException(id));

        List<ShelterDTOById> collect = shelterRepository.findById(id)
                .stream()
                .map(shelterDTOByIdMapper)
                .toList();

        return collect.stream().findFirst().orElseThrow(() -> new ShelterNotFoundException(id));
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
