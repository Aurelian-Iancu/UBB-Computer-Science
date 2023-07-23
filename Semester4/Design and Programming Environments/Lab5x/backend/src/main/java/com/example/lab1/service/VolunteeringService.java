package com.example.lab1.service;

import com.example.lab1.exceptions.ShelterNotFoundException;
import com.example.lab1.exceptions.VolunteerNotFoundException;
import com.example.lab1.model.KeyVolunteering;
import com.example.lab1.model.Shelter;
import com.example.lab1.model.Volunteer;
import com.example.lab1.model.Volunteering;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerVolunteeringDTO;
import com.example.lab1.repository.ShelterRepository.ShelterRepository;
import com.example.lab1.repository.VolunteerRepository;
import com.example.lab1.repository.VolunteeringRepository;
import org.springframework.stereotype.Service;

@Service
public class VolunteeringService {

    private final ShelterRepository shelterRepository;

    private final VolunteerRepository volunteerRepository;

    private final VolunteeringRepository volunteeringRepository;

    public VolunteeringService(ShelterRepository shelterRepository,
                               VolunteerRepository volunteerRepository,
                               VolunteeringRepository volunteeringRepository) {
        this.shelterRepository = shelterRepository;
        this.volunteerRepository = volunteerRepository;
        this.volunteeringRepository = volunteeringRepository;
    }

    public Volunteering createVolunteering(VolunteerVolunteeringDTO volunteer, Long shelterId){
        //check for shelter existent and volunteer existent
        Shelter shelter = this.shelterRepository.findById(shelterId).orElseThrow(() -> new ShelterNotFoundException(shelterId));
        Volunteer volunteerFromDB = this.volunteerRepository.findById(volunteer.getVolunteerId()).orElseThrow(() -> new VolunteerNotFoundException(shelterId));

        //create key
        KeyVolunteering keyVolunteering = new KeyVolunteering();
        keyVolunteering.setVolunteerId(volunteer.getVolunteerId());
        keyVolunteering.setShelterId(shelterId);

        //create volunteering
        Volunteering volunteering = new Volunteering();
        volunteering.setID(keyVolunteering);
        volunteering.setShelter(shelter);
        volunteering.setVolunteer(volunteerFromDB);
        volunteering.setRole(volunteer.getRole());
        volunteering.setHoursPerWeek(volunteer.getHoursPerWeek());

        this.volunteeringRepository.save(volunteering);

        //add the volunteering to the lists from shelter and volunteer
        shelter.addVolunteering(volunteering);
        volunteerFromDB.addVolunteering(volunteering);

        return volunteering;
    }
}
