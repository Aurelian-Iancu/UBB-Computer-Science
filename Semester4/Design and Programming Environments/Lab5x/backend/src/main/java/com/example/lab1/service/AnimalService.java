package com.example.lab1.service;

import com.example.lab1.exceptions.AnimalNotFoundException;
import com.example.lab1.exceptions.ShelterNotFoundException;
import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.animalDTO.AnimalDTOIdShelter;
import com.example.lab1.repository.AnimalRepository;
import com.example.lab1.repository.ShelterRepository.ShelterRepository;
import com.example.lab1.service.mappers.animalMappers.AnimalDTOIdShelterMapper;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import org.springframework.data.domain.Pageable;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class AnimalService {
    private final AnimalRepository animalRepository;
    private final ShelterRepository shelterRepository;
    private final AnimalDTOIdShelterMapper animalDTOIdShelterMapper;

    public AnimalService(AnimalRepository animalRepository,
                         ShelterRepository shelterRepository,
                         AnimalDTOIdShelterMapper animalDTOIdShelterMapper) {
        this.animalRepository = animalRepository;
        this.shelterRepository = shelterRepository;
        this.animalDTOIdShelterMapper = animalDTOIdShelterMapper;
    }



    public List<AnimalDTOIdShelter> findAllAnimals(Integer pageNo, Integer pageSize){
        Pageable pageable = PageRequest.of(pageNo, pageSize, Sort.by("animalId"));

        return this.animalRepository.findAll(pageable)
                .getContent()
                .stream()
                .map(
                animalDTOIdShelterMapper
        ).collect(Collectors.toList());

    }

    public Animal findAnimalById(Long id){

        List<Animal> collect = animalRepository.findByAnimalId(id)
                .stream().toList();

//        List<ShelterDTOById> collect = shelterRepository.findById(id)
//                .stream()
//                .map(shelterDTOByIdMapper)
//                .toList();

        return collect.stream().findFirst().orElseThrow(() -> new AnimalNotFoundException(id));
    }

    public Animal saveAnimal(Animal animal, Long id) {
        return this.shelterRepository.findById(id)
                .map(shelter -> {
                    animal.setShelter(shelter);
                    shelter.addAnimal(animal);
                    return this.animalRepository.save(animal);
                }).orElseThrow(() -> new ShelterNotFoundException(id));
    }

    public Animal updateAnimal(Animal animal, Long id){
        Animal oldAnimal = animalRepository.findById(id).orElseThrow(() -> new AnimalNotFoundException(id));
        if(oldAnimal != null) {
            oldAnimal.setName(animal.getName());
            oldAnimal.setType(animal.getType());
            oldAnimal.setWeight(animal.getWeight());
            oldAnimal.setDateOfBirth(animal.getDateOfBirth());
            animalRepository.save(oldAnimal);
            return oldAnimal;
        }

        return animalRepository.save(animal);
    }

    public void deleteAnimal(Long id){

        Shelter shelter = null;
        Animal animal = this.animalRepository.findById(id).orElseThrow(() -> new AnimalNotFoundException(id));
        if(animal != null) {
            shelter = this.shelterRepository.findById(animal.getShelter().getShelterId())
                    .orElseThrow(() -> new ShelterNotFoundException(id));
        }
        if(shelter != null){
            shelter.removeAnimal(animal);
        }
        this.animalRepository.deleteById(id);
    }

    public List<AnimalDTOIdShelter> findByWeightGreaterThan(Double weight, Integer pageNo, Integer pageSize){
        Pageable pageable = (Pageable) PageRequest.of(pageNo, pageSize, Sort.by("animalId"));

        return this.animalRepository.findByWeightGreaterThan(weight, pageable).
                getContent()
                .stream()
                .map(animalDTOIdShelterMapper)
                .collect(Collectors.toList());
    }

    /*public Shelter updateShelter(Long animalId, Long shelterId) {
        //get Animal
        Animal animal = this.animalRepository.findById(animalId).orElseThrow(() -> new AnimalNotFoundException(animalId));

        //get the old shelter
        Long oldShelterId = animal.getShelter().getShelterId();
        Shelter oldShelter = this.shelterRepository.findById(oldShelterId).orElseThrow(() -> new ShelterNotFoundException(oldShelterId));

        //get new shelter
        Shelter shelter = this.shelterRepository.findById(shelterId).orElseThrow(() -> new ShelterNotFoundException(shelterId));

        oldShelter.removeAnimal(animal);
        shelter.addAnimal(animal);
        animal.setShelter(shelter);

        return oldShelter;
    }*/
}
