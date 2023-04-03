package com.example.lab1.modelDTO.volunteerDTO;

import com.example.lab1.modelDTO.shelterDTO.ShelterDTOWithVolunteering;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Set;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class VolunteerDTO_forOne {
    Long volunteerId;
    String firstName;
    String lastName;
    String email;
    Long phone;
    String nationality;
    private Set<ShelterDTOWithVolunteering> shelters;
}
