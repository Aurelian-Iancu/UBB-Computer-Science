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
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping("/api/shelter")

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
    ResponseEntity<List<ShelterDTOAll>> findAllShelters(@RequestParam(defaultValue = "0") Integer pageNo,
                                                        @RequestParam(defaultValue = "10") Integer pageSize){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.shelterService.findAllShelters(pageNo, pageSize));
    }

    //get shelter by id with all the animals that live there
    @GetMapping("/{id}")
    ResponseEntity<ShelterDTOById> findShelterById(@PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(shelterService.findShelterById(id));
    }

    @GetMapping("/statistics/countAnimal")
    ResponseEntity<List<ShelterDTOCount>> getSheltersOrderedByNumberOfAnimalsAsc(){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.shelterService.getSheltersOrderedByNumberOfAnimalsAsc());
    }

    @GetMapping("/statistics/averageWeight")
    ResponseEntity<List<ShelterDTOAverage>> getSheltersOrderedByAverageWeightDesc(){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.shelterService.getSheltersOrderedByAverageWeightDesc());
    }

    //add shelter to database
    @PostMapping("/save")
    ResponseEntity<Shelter> saveShelter(@Valid @RequestBody Shelter shelter){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(shelterService.saveShelter(shelter));}

    //add volunteering for a shelter and a volunteer
    @PostMapping("/save/shelter/{id}/volunteer")
    ResponseEntity<Volunteering> newVolunteerVolunteering(@RequestBody VolunteerVolunteeringDTO volunteer, @PathVariable Long id) {
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.volunteeringService.createVolunteering(volunteer, id));
    }

    //update shelter by id
    @PutMapping("/update/{id}")
    ResponseEntity<Shelter> updateShelter(@Valid @RequestBody Shelter shelter, @PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(shelterService.updateShelter(shelter, id));
    }

    //delete shelter by id
    @DeleteMapping("/delete/{id}")
    ResponseEntity<HttpStatus> deleteShelter(@PathVariable("id") Long id){
        this.shelterService.deleteShelter(id);
        return ResponseEntity.accepted().body(HttpStatus.OK);

    }
}
