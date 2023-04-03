package com.example.lab1.service.mappers.volunteerMappers;

import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTO;
import org.springframework.stereotype.Service;

import java.util.function.Function;
@Service
public class VolunteerDTOMapper implements Function<Volunteer, VolunteerDTO> {
    @Override
    public VolunteerDTO apply(Volunteer volunteer) {
        return new VolunteerDTO(
                volunteer.getVolunteerId(),
                volunteer.getFirstName(),
                volunteer.getLastName(),
                volunteer.getEmail(),
                volunteer.getPhone(),
                volunteer.getNationality()
        );
    }
}
