package com.example.lab1.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
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
@Table(name = "shelter")
public class Shelter {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long shelterId;
    @Column
    private String name;
    @Column
    private String address;
    @Column
    private Integer numberOfVolunteers;
    @Column
    private Integer capacity;
    @Column
    private String city;


    @OneToMany(mappedBy = "shelter", cascade = CascadeType.REMOVE)
    @JsonIgnore
    protected List<Animal> animals;

    @OneToMany(mappedBy = "shelter")
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
