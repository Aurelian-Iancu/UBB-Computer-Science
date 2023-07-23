package com.example.lab1.model;

import jakarta.persistence.*;
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
    private int animalId;
    @Column
    private String name;
    @Column
    private String type;
    @Column
    private Double weight;
    @Column
    private String dateOfBirth;

    @ManyToOne
    @JoinColumn(name = "shelter_animal_fk", nullable = false)
    private Shelter shelter;


}