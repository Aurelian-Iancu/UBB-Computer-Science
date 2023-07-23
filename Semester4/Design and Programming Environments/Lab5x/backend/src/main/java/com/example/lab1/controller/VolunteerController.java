package com.example.lab1.controller;

import com.example.lab1.model.Shelter;
import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAll;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOById;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOWithVolunteering;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTOSimple;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTO_forOne;
import com.example.lab1.service.ShelterService;
import com.example.lab1.service.VolunteerService;

import org.modelmapper.ModelMapper;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping("/api/volunteer")
public class VolunteerController {
    private final VolunteerService volunteerService;

    private final ShelterService shelterService;

    private final ModelMapper modelMapper;

    public VolunteerController(VolunteerService volunteerService,
                               ShelterService shelterService,
                               ModelMapper modelMapper) {
        this.volunteerService = volunteerService;
        this.shelterService = shelterService;
        this.modelMapper = modelMapper;
    }

    //get all the volunteers only with their info
    @GetMapping("/getAll")
    ResponseEntity<List<VolunteerDTOSimple>> findAllVolunteers(@RequestParam(defaultValue = "0") Integer pageNo,
                                                               @RequestParam(defaultValue = "10") Integer pageSize){

        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.volunteerService.findAllVolunteers(pageNo, pageSize));
    }


    @GetMapping("/{id}")
    ResponseEntity<VolunteerDTO_forOne> findVolunteerById(@PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.convertToReaderDTO_forOne(this.volunteerService.findVolunteerById(id)));
    }

    //add new volunteer to database
    @PostMapping("/save")
    ResponseEntity<Volunteer> saveVolunteer(@RequestBody Volunteer volunteer){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(volunteerService.saveVolunteer(volunteer));
    }

    //update volunteer by id
    @PutMapping("/update/{id}")
    ResponseEntity<Volunteer> updateVolunteer(@RequestBody Volunteer volunteer, @PathVariable("id") Long id){
        return ResponseEntity
                .status(HttpStatus.OK)
                .body(this.volunteerService.updateVolunteer(volunteer, id));
    }

    //delete volunteer by id
    @DeleteMapping("/delete/{id}")
    ResponseEntity<HttpStatus> deleteVolunteer(@PathVariable("id") Long id){
        this.volunteerService.deleteVolunteer(id);
        return ResponseEntity.accepted().body(HttpStatus.OK);
    }

    private VolunteerDTO_forOne convertToReaderDTO_forOne(Volunteer volunteer){
        VolunteerDTO_forOne volunteerDTO = this.modelMapper.map(volunteer, VolunteerDTO_forOne.class);
        Set<ShelterDTOWithVolunteering> shelters = volunteer.getVolunteerings().stream()
                .map((volunteering -> {
                    ShelterDTOById shelter = this.shelterService.findShelterById(volunteering.getID().getVolunteerId());
                    ShelterDTOWithVolunteering shelterDTO = new ShelterDTOWithVolunteering();
                    shelterDTO.setShelterId(shelter.shelterId());
                    shelterDTO.setName(shelter.name());
                    shelterDTO.setAddress(shelter.address());
                    shelterDTO.setNumberOfVolunteers(shelter.numberOfVolunteers());
                    shelterDTO.setCapacity(shelter.capacity());
                    shelterDTO.setCity(shelter.city());
                    shelterDTO.setHoursPerWeek(volunteering.getHoursPerWeek());
                    shelterDTO.setRole(volunteering.getRole());
                    return shelterDTO;
                })).collect(Collectors.toSet());
        volunteerDTO.setShelters(shelters);
        return volunteerDTO;
    }
}
