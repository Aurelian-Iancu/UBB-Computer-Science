package com.example.lab1.service;

import com.example.lab1.exceptions.AnimalNotFoundException;
import com.example.lab1.exceptions.ShelterNotFoundException;
import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.animalDTO.AnimalDTOIdShelter;
import com.example.lab1.repository.AnimalRepository;
import com.example.lab1.repository.ShelterRepository;
import com.example.lab1.service.mappers.animalMappers.AnimalDTOIdShelterMapper;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
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



    public List<AnimalDTOIdShelter> findAllAnimals(){
        return animalRepository.findAll()
                .stream()
                .map(animalDTOIdShelterMapper).
                collect(Collectors.toList());
    }

    public Optional<Animal> findAnimalById(Long id){
        return animalRepository.findById(id);
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

    public List<Animal> findByWeightGreaterThan(Double weight){
        return this.animalRepository.findByWeightGreaterThan(weight);
    }

    public Shelter updateShelter(Long animalId, Long shelterId) {
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
    }
}
