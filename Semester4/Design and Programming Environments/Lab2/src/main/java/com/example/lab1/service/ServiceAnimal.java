package com.example.lab1.service;

import com.example.lab1.model.EntityAnimal;
import com.example.lab1.repository.RepositoryAnimal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ServiceAnimal {

    private final RepositoryAnimal repositoryAnimal;

    public ServiceAnimal(RepositoryAnimal repositoryAnimal) {
        this.repositoryAnimal = repositoryAnimal;
    }

    public List<EntityAnimal> findAllAnimals(){
        return repositoryAnimal.findAll();
    }

    public Optional<EntityAnimal> findById(Long id){
        return repositoryAnimal.findById(id);
    }

    public EntityAnimal saveAnimal(EntityAnimal entityAnimal) {
        return repositoryAnimal.save(entityAnimal);
    }

    public EntityAnimal updateAnimal(EntityAnimal entityAnimal, Long id){
        EntityAnimal oldAnimal = repositoryAnimal.findById(id).orElse(null);
        if(oldAnimal != null) {
            oldAnimal.setName(entityAnimal.getName());
            oldAnimal.setType(entityAnimal.getType());
            oldAnimal.setWeight(entityAnimal.getWeight());
            oldAnimal.setDateOfBirth(entityAnimal.getDateOfBirth());
            repositoryAnimal.save(oldAnimal);
            return oldAnimal;

        }

        return repositoryAnimal.save(entityAnimal);
    }

    public void deleteAnimal(Long id){
        repositoryAnimal.deleteById(id);
    }
}
