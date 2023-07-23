package com.example.lab1.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.NotEmpty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.util.List;


@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
//Database part
@Entity
@Table(name = "shelter", indexes = {
        @Index(name = "name_shelters_index", columnList = "name")
})
public class Shelter {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long shelterId;

    @Column
    @NotEmpty
    private String name;

    @Column
    private String address;

    @Column
    private Integer numberOfVolunteers;

    @Column
    @Max(100)
    private Integer capacity;

    @Column
    private String city;

    @Column(length = 2000)
    @NotEmpty
    private String description;


    @OneToMany(mappedBy = "shelter", cascade = CascadeType.REMOVE, fetch = FetchType.LAZY)
    @JsonIgnore
    protected List<Animal> animals;

    @OneToMany(mappedBy = "shelter", fetch = FetchType.LAZY)
    @JsonIgnore
    private List<Volunteering> volunteerings;

    public void addAnimal(Animal animal){
        this.animals.add(animal);
    }

    public void removeAnimal(Animal animal){
        this.animals.remove(animal);
    }

    public void addVolunteering(Volunteering volunteering){
        this.volunteerings.add(volunteering);
    }
}
