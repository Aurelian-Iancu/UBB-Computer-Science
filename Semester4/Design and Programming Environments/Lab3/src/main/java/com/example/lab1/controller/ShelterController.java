package com.example.lab1.controller;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.model.Volunteering;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAll;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOById;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerVolunteeringDTO;
import com.example.lab1.service.AnimalService;
import com.example.lab1.service.ShelterService;
import com.example.lab1.service.VolunteeringService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/shelter")
public class ShelterController {
    private final ShelterService shelterService;

    private final VolunteeringService volunteeringService;

    public ShelterController(ShelterService shelterService,
                             VolunteeringService volunteeringService) {
        this.shelterService = shelterService;
        this.volunteeringService = volunteeringService;
    }

    //get all shelters without any information about the animals
    @GetMapping("/getAll")
    public List<ShelterDTOAll> findAllShelters(){
        return shelterService.findAllShelters();
    }

    //get shelter by id with all the animals that live there
    @GetMapping("/getById/{id}")
    public Optional<ShelterDTOById> findShelterById(@PathVariable("id") Long id){
        return shelterService.findShelterById(id);
    }

    @GetMapping("/statistics-countAnimal")
    public List<ShelterDTOCount> getSheltersOrderedByNumberOfAnimalsAsc(){
        return this.shelterService.getSheltersOrderedByNumberOfAnimalsAsc();
    }

    @GetMapping("/statistics-averageWeight")
    public List<ShelterDTOAverage> getSheltersOrderedByAverageWeightDesc(){
        return this.shelterService.getSheltersOrderedByAverageWeightDesc();
    }

    //add shelter to database
    @PostMapping("/save")
    public Shelter saveShelter(@RequestBody Shelter shelter){
        return shelterService.saveShelter(shelter);
    }

    //add volunteering for a shelter and a volunteer
    @PostMapping("/save/shelter/{id}/volunteer")
    public Volunteering newVolunteerVolunteering(@RequestBody VolunteerVolunteeringDTO volunteer, @PathVariable Long id) {
        return this.volunteeringService.createVolunteering(volunteer, id);
    }

    //update shelter by id
    @PutMapping("/update/{id}")
    public Shelter updateShelter(@RequestBody Shelter shelter, @PathVariable("id") Long id){
        return shelterService.updateShelter(shelter, id);
    }

    //delete shelter by id
    @DeleteMapping("/delete/{id}")
    public void deleteShelter(@PathVariable("id") Long id){
        this.shelterService.deleteShelter(id);
    }
}
