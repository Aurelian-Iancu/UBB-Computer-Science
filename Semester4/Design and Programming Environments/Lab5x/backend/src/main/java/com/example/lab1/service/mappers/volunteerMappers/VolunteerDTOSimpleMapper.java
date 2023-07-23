package com.example.lab1.service.mappers.volunteerMappers;

import com.example.lab1.model.Volunteer;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTOSimple;
import org.springframework.stereotype.Service;

import java.util.function.Function;
@Service
public class VolunteerDTOSimpleMapper implements Function<Volunteer, VolunteerDTOSimple> {
    @Override
    public VolunteerDTOSimple apply(Volunteer volunteer) {
        return new VolunteerDTOSimple(
                volunteer.getVolunteerId(),
                volunteer.getFirstName(),
                volunteer.getLastName(),
                volunteer.getEmail(),
                volunteer.getPhone(),
                volunteer.getCountry()
        );
    }
}
