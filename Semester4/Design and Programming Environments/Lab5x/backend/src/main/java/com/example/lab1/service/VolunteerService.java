package com.example.lab1.service;

import com.example.lab1.exceptions.VolunteerNotFoundException;
import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTOSimple;
import com.example.lab1.repository.VolunteerRepository;
import com.example.lab1.service.mappers.volunteerMappers.VolunteerDTOSimpleMapper;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class VolunteerService {

    private final VolunteerRepository volunteerRepository;

    private final VolunteerDTOSimpleMapper volunteerDTOSimpleMapper;

    public VolunteerService(VolunteerRepository volunteerRepository,
                            VolunteerDTOSimpleMapper volunteerDTOSimpleMapper) {
        this.volunteerRepository = volunteerRepository;
        this.volunteerDTOSimpleMapper = volunteerDTOSimpleMapper;
    }



    public List<VolunteerDTOSimple> findAllVolunteers(Integer pageNo, Integer pageSize){
        Pageable pageable = PageRequest.of(pageNo, pageSize, Sort.by("volunteerId"));
        return this.volunteerRepository.findAll(pageable)
                .getContent()
                .stream()
                .map(volunteerDTOSimpleMapper)
                .collect(Collectors.toList());
    }

    public Volunteer findVolunteerById(Long id){
        return this.volunteerRepository.findById(id).orElseThrow(() -> new VolunteerNotFoundException(id));
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
            oldVolunteer.setCountry(volunteer.getCountry());
            volunteerRepository.save(oldVolunteer);
            return oldVolunteer;
        }
        return volunteerRepository.save(volunteer);
    }

    public void deleteVolunteer(Long id){
        volunteerRepository.deleteById(id);
    }
}
