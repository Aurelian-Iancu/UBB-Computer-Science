import { Shelter } from "./Shelter";

export interface AnimalWShelter{
    animalId: number;
    name: string;
    type: string;
    weight: number; 
    dateOfBirth: string;
    breed: string;
    shelter: Shelter;
}