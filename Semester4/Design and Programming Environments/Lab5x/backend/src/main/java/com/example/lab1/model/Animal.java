package com.example.lab1.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Past;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import org.springframework.format.annotation.DateTimeFormat;

import java.time.LocalDate;


@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
//Database part
@Entity
@Table(name = "animal", indexes = {
        @Index(name = "fk_animal_shelter_index", columnList = "shelter_animal_fk"),
        @Index(name = "weight_animals_index", columnList = "weight")
})
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
    private String breed;

    @Column
    @Past
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private LocalDate dateOfBirth;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "shelter_animal_fk", nullable = false)
    private Shelter shelter;

    public Animal(Long animalId, String name, String type, Double weight, String dateOfBirth, String breed) {
    }
}
