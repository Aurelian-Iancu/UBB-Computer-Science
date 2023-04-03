package com.example.lab1.modelDTO.volunteerDTO;

import jakarta.persistence.Column;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class VolunteerDTO_withMembership {
    private Long volunteerId;
    private String firstName;
    private String lastName;
    private String email;
    private Long phone;
    private String nationality;
    private Integer hoursPerWeek;
    private String role;
}
