package com.example.lab1.modelDTO.shelterDTO;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ShelterDTOCount {
    private String shelterName;
    private Long count;
}
