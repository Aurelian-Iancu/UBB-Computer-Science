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
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Shelter } from "../../models/Shelter";
import EditIcon from "@mui/icons-material/Edit";
import VisibilityIcon from '@mui/icons-material/Visibility';
import DeleteIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import FilterAltIcon from '@mui/icons-material/FilterAlt';
import { ShelterOrdNoAnimals } from "../../models/ShelterOrdNoAnimals";

export const ShelterStatisticsCountAnimal = () => {
    const[loading, setLoading] = useState(true);
    const[shelters, setShelters] = useState([]);

    useEffect(() => {
        fetch(`${BACKEND_API_URL}/shelter/statistics/countAnimal`)
            .then(res => res.json())
            .then(data => {setShelters(data); setLoading(false);})
    }, []);

    console.log(shelters);

    return (

        <Container>
            <h1 style={{marginTop:"65px"}}>Shelters ordered by number of animals</h1>

            {loading && <CircularProgress />}

            {!loading && shelters.length == 0 && <div>No shelters found</div>}

            {!loading && shelters.length > 0 && (

                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 800 }} aria-label="simple table" style={{backgroundColor:"whitesmoke"}}>
                        <TableHead>
                            <TableRow>
                                <TableCell align="left" style={{color:"#2471A3", fontWeight:'bold'}}>Crt.</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Name</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Number of animals</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {shelters.map((shelter:ShelterOrdNoAnimals, index) => (
                                <TableRow key={shelter.shelterName}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{shelter.shelterName}</TableCell>
                                    <TableCell align="center">{shelter.count}</TableCell>
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