import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Animal } from "../../models/Animals";

export const AnimalFilter = () => {
    const { weight } = useParams();

    const[loading, setLoading] = useState(true);
    const[animals, setAnimals] = useState([]);


    useEffect(() => {
        fetch(`${BACKEND_API_URL}/animal/getAll?minWeight=${weight}`)
            .then(res => res.json())
            .then(data => {setAnimals(data); setLoading(false);})
    }, []);

    console.log(animals);

    return (

        <Container>
            <h1 style={{marginTop:"65px"}}>Animal with weight greater than ${weight} </h1>

            {loading && <CircularProgress />}

            {!loading && animals.length == 0 && <div>No animals found</div>}

            {!loading && animals.length > 0 && (

                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 800 }} aria-label="simple table" style={{backgroundColor:"whitesmoke"}}>
                        <TableHead>
                            <TableRow>
                            <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Crt.</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Name</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Type</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Weight</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Date of birth</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Breed</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {animals.map((animal:Animal, index) => (
                                <TableRow key={animal.name}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{animal.name}</TableCell>
                                    <TableCell align="center">{animal.type}</TableCell>
                                    <TableCell align="center">{animal.weight}</TableCell>
                                    <TableCell align="center">{animal.dateOfBirth}</TableCell>
                                    <TableCell align="center">{animal.breed}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )
            }
        </Container>

    );
}