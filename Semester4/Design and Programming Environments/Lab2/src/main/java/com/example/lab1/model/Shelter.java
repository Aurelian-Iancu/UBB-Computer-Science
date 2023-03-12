package com.example.lab1.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.util.Set;


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
    private int shelterId;
    @Column
    private String name;
    @Column
    private String address;
    @Column
    private int numberOfEmployees;
    @Column
    private int capacity;

    @OneToMany(mappedBy = "shelter", cascade = CascadeType.ALL)
    @JsonIgnore
    private Set<Animal> animals;
}
