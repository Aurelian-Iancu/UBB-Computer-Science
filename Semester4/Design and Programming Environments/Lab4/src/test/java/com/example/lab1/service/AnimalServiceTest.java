package com.example.lab1.service;


import com.example.lab1.model.Animal;
import com.example.lab1.repository.AnimalRepository;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.mock.mockito.MockBean;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@RunWith(MockitoJUnitRunner.class)
public class AnimalServiceTest {
    @Mock
    private AnimalRepository animalRepository;

    @InjectMocks
    private AnimalService animalService;

    @Before
    public void init() {
        when(this.animalRepository.findByWeightGreaterThan(10.0)).thenReturn(Arrays.asList(
                new Animal(1L, "name1", "type1", 11.0, "2002", "breed1", null),
                new Animal(2L, "name2", "type2", 12.0, "2002", "breed2", null),
                new Animal(3L, "name3", "type1", 13.0, "2002", "breed3", null),
                new Animal(4L, "name4", "type1", 54.0, "2002", "breed4", null)
        ));
    }

    @Test
    public void testGetAnimalsWithHigherWeight() {

        List<Animal> result = this.animalService.findByWeightGreaterThan(10.0);


        assertEquals(4, result.size());
        assertEquals("name1", result.get(0).getName());
        assertEquals("name2", result.get(1).getName());
        assertEquals("name3", result.get(2).getName());
        assertEquals("name4", result.get(3).getName());

        assertEquals(54.0, result.get(3).getWeight());
    }
}
