package com.example.lab1.service;

import com.example.lab1.exceptions.VolunteerNotFoundException;
import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTO;
import com.example.lab1.repository.VolunteerRepository;
import com.example.lab1.service.mappers.volunteerMappers.VolunteerDTOMapper;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class VolunteerService {

    private final VolunteerRepository volunteerRepository;

    private final VolunteerDTOMapper volunteerDTOMapper;

    public VolunteerService(VolunteerRepository volunteerRepository,
                            VolunteerDTOMapper volunteerDTOMapper) {
        this.volunteerRepository = volunteerRepository;
        this.volunteerDTOMapper = volunteerDTOMapper;
    }



    public List<VolunteerDTO> findAllVolunteers(){
        return this.volunteerRepository.findAll()
                .stream()
                .map(volunteerDTOMapper)
                .collect(Collectors.toList());
    }

    public Optional<Volunteer> findVolunteerById(Long id){
        return this.volunteerRepository.findById(id);
    }

    public Volunteer saveVolunteer(Volunteer volunteer){
        return this.volunteerRepository.save(volunteer);
    }

    public Volunteer updateVolunteer(Volunteer volunteer, Long id){
        Volunteer oldVolunteer = volunteerRepository.findById(id).orElseThrow(() -> new VolunteerNotFoundException(id));
        if(oldVolunteer != null){
            oldVolunteer.setFirstName(volunteer.getFirstName());
            oldVolunteer.setLastName(volunteer.getLastName());
            oldVolunteer.setEmail(volunteer.getEmail());
            oldVolunteer.setEmail(volunteer.getEmail());
            oldVolunteer.setNationality(volunteer.getNationality());
            volunteerRepository.save(oldVolunteer);
            return oldVolunteer;
        }
        return volunteerRepository.save(volunteer);
    }

    public void deleteVolunteer(Long id){
        volunteerRepository.deleteById(id);
    }
}
