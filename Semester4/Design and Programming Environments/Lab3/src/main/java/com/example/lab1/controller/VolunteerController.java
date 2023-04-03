package com.example.lab1.controller;

import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTO;
import com.example.lab1.service.VolunteerService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/volunteer")
public class VolunteerController {
    private final VolunteerService volunteerService;

    public VolunteerController(VolunteerService volunteerService) {
        this.volunteerService = volunteerService;
    }

    //get all the volunteers only with their info
    @GetMapping("/getAll")
    public List<VolunteerDTO> findAllVolunteers(){
        return this.volunteerService.findAllVolunteers();
    }


    @GetMapping("/getById/{id}")
    public Optional<Volunteer> findVolunteerById(@PathVariable("id") Long id){
        return this.volunteerService.findVolunteerById(id);
    }

    //add new volunteer to database
    @PostMapping("/save")
    public Volunteer saveVolunteer(@RequestBody Volunteer volunteer){
        return volunteerService.saveVolunteer(volunteer);
    }

    //update volunteer by id
    @PutMapping("/update/{id}")
    public Volunteer updateVolunteer(@RequestBody Volunteer volunteer, @PathVariable("id") Long id){
        return this.volunteerService.updateVolunteer(volunteer, id);
    }

    //delete volunteer by id
    @DeleteMapping("/delete/{id}")
    public void deleteVolunteer(@PathVariable("id") Long id){
        this.volunteerService.deleteVolunteer(id);
    }
}
