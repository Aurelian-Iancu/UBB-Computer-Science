package com.example.lab1.modelDTO.shelterDTO;

import com.example.lab1.model.Animal;
import com.example.lab1.modelDTO.volunteerDTO.VolunteerDTO_withMembership;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;
import java.util.Set;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ShelterDTOEverything {
    private Long shelterId;
    private String name;
    private String address;
    private Integer numberOfVolunteers;
    private Integer capacity;
    private String city;
    private String description;
    private List<Animal> animals;
    private Set<VolunteerDTO_withMembership> volunteerings;
}
