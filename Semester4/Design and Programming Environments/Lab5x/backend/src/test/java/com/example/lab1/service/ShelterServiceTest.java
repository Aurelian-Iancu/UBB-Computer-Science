package com.example.lab1.service;

import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;
import com.example.lab1.repository.ShelterRepository.ShelterRepositoryCustom;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;

import java.util.Arrays;
import java.util.List;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

@RunWith(MockitoJUnitRunner.class)
public class ShelterServiceTest {
    @Mock
    private ShelterRepositoryCustom shelterRepository;

    @InjectMocks
    private ShelterService shelterService;

    @Before
    public void init(){
        when(this.shelterRepository.findSheltersOrderedByNumberOfAnimalsAsc()).thenReturn(Arrays.asList(
                new ShelterDTOCount("name1", 5L),
                new ShelterDTOCount("name2", 6L),
                new ShelterDTOCount("name3", 10L)
        ));

        when(this.shelterRepository.findSheltersOrderedByAverageWeightDesc()).thenReturn(Arrays.asList(
                new ShelterDTOAverage("name1", 11.1),
                new ShelterDTOAverage("name2", 5.2),
                new ShelterDTOAverage("name3", 2.6)
        ));
    }

    @Test
    public void testGetSheltersOrderedAscendingByAnimalNumber(){
        List<ShelterDTOCount> result = this.shelterService.getSheltersOrderedByNumberOfAnimalsAsc();

        assertEquals(3, result.size());
        assertEquals("name1", result.get(0).getShelterName());
        assertEquals("name2", result.get(1).getShelterName());
        assertEquals("name3", result.get(2).getShelterName());
    }

    @Test
    public void testGetSheltersOrderedDescendingByAverageWeight(){
        List<ShelterDTOAverage> result = this.shelterService.getSheltersOrderedByAverageWeightDesc();

        assertEquals(3, result.size());
        assertEquals("name1", result.get(0).getAnimalName());
        assertEquals("name2", result.get(1).getAnimalName());
        assertEquals("name3", result.get(2).getAnimalName());
    }
}
