package com.example.lab1.modelDTO.volunteerDTO;

import lombok.Data;

@Data
public class VolunteerVolunteeringDTO
{
    private Long volunteerId;
    private String firstName;
    private String lastName;
    private String email;
    private Long phone;
    private String nationality;
    private Integer hoursPerWeek;
    private String role;
}
