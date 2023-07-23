package com.example.lab1.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "volunteers_in", indexes = {
        @Index(name = "fk_volunteer_id_membership_index", columnList = "volunteer_id"),
        @Index(name = "fk_shelter_id_membership_index", columnList = "shelter_id")
})
public class Volunteering {
    @EmbeddedId
    private KeyVolunteering ID;

    @ManyToOne
    @MapsId("volunteerId")
    @JsonIgnore
    @JoinColumn(name = "volunteer_id")
    private Volunteer volunteer;

    @ManyToOne
    @MapsId("shelterId")
    @JsonIgnore
    @JoinColumn(name = "shelter_id")
    private Shelter shelter;

    @Column
    private Integer hoursPerWeek;
    @Column
    private String role;
}
