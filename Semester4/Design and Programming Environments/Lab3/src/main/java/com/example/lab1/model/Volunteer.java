package com.example.lab1.model;

import com.example.lab1.modelDTO.volunteerDTO.VolunteerVolunteeringDTO;
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
@Table(name = "volunteer")
public class Volunteer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long volunteerId;
    @Column
    private String firstName;
    @Column
    private String lastName;
    @Column
    private String email;
    @Column
    private Long phone;
    @Column
    private String nationality;


    @OneToMany(mappedBy = "volunteer")
    @JsonIgnore
    private List<Volunteering> volunteerings;

    public void addVolunteering(Volunteering volunteering){
        this.volunteerings.add(volunteering);
    }
}
