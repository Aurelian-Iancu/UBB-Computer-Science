package com.example.lab1.model;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Embeddable
public class KeyVolunteering implements Serializable {
    @Column(name = "shelter_id")
    private Long shelterId;
    @Column(name = "volunteer_id")
    private Long volunteerId;
}
