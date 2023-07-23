import { Animal } from "./Animals";

export interface Shelter{
    shelterId:number;
    name: string;
    address: string;
    numberOfVolunteers: number;
    capacity: number;
    city: string;
    description: string;
    animals ?: Animal[];
}