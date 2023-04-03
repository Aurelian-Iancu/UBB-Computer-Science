package com.example.lab1.repository;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOAverage;
import com.example.lab1.modelDTO.shelterDTO.ShelterDTOCount;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.criteria.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class ShelterRepositoryCustomImpl implements ShelterRepositoryCustom{
    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<ShelterDTOCount> findSheltersOrderedByNumberOfAnimalsAsc() {
        CriteriaBuilder cb = this.entityManager.getCriteriaBuilder();
        CriteriaQuery<ShelterDTOCount> query = cb.createQuery(ShelterDTOCount.class);
        Root<Shelter> shelterRoot = query.from(Shelter.class);
        Join<Shelter, Animal> shelterAnimalJoin = shelterRoot.join("animals", JoinType.INNER);

        query.select(cb.construct(
                ShelterDTOCount.class,
                shelterRoot.get("name"),
                cb.count(shelterAnimalJoin.get("name"))
        ))
                .groupBy(shelterRoot.get("name"))
                .orderBy(cb.asc(cb.count(shelterAnimalJoin.get("name"))));


        return this.entityManager.createQuery(query).getResultList();
    }

    @Override
    public List<ShelterDTOAverage> findSheltersOrderedByAverageWeightDesc() {
        CriteriaBuilder cb = this.entityManager.getCriteriaBuilder();
        CriteriaQuery<ShelterDTOAverage> query = cb.createQuery(ShelterDTOAverage.class);
        Root<Shelter> shelterRoot = query.from(Shelter.class);
        Join<Shelter, Animal> shelterAnimalJoin = shelterRoot.join("animals", JoinType.INNER);

        query.select(cb.construct(
                        ShelterDTOAverage.class,
                        shelterRoot.get("name"),
                        cb.avg(shelterAnimalJoin.get("weight"))
                ))
                .groupBy(shelterRoot.get("name"))
                .orderBy(cb.asc(cb.avg(shelterAnimalJoin.get("weight"))));

        return this.entityManager.createQuery(query).getResultList();
    }
}
