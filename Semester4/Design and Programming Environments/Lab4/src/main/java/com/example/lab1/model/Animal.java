package com.example.lab1.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;


@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
//Database part
@Entity
@Table(name = "animal")
public class Animal {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long animalId;

    @Column
    @NotEmpty
    private String name;

    @Column
    @NotEmpty
    private String type;

    @Column
    @Min(0)
    private Double weight;

    @Column
    private String dateOfBirth;

    @Column
    private String breed;

    @ManyToOne
    @JoinColumn(name = "shelter_animal_fk", nullable = false)
    private Shelter shelter;

    public Animal(Long animalId, String name, String type, Double weight, String dateOfBirth, String breed) {
    }
}
