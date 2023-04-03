package com.example.lab1.modelDTO.volunteerDTO;

public record VolunteerDTO (
        Long volunteerId,
        String firstName,
        String lastName,
        String email,
        Long phone,
        String nationality
) {
}
