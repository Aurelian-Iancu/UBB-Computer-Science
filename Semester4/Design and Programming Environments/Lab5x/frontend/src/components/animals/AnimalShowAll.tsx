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
    Button,
} from "@mui/material";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Animal } from "../../models/Animals";
import EditIcon from "@mui/icons-material/Edit";
import VisibilityIcon from '@mui/icons-material/Visibility';
import DeleteIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import FilterAltIcon from '@mui/icons-material/FilterAlt';
import TextField from "@mui/material/TextField";
import Box from '@mui/material/Box';
import { Paginator } from "../pagination/pagination";



export const AnimalsShowAll = () => {
    const[loading, setLoading] = useState(true);
    const[animals, setAnimals] = useState([]);
    const[pageSize, setPageSize] = useState(10);
    const[total, setTotal] = useState(0);
    const[currentPage, setCurrentPage] = useState(0);

    const handlePreviousPage = () => {
        if(currentPage>0)
        {
          setCurrentPage(currentPage-1);
        }
      };
    
      const handleNextPage = () => {
        setCurrentPage(currentPage+1);
      };

      useEffect(() => {
        setLoading(true);
    
        const fetchAnimals = () => {
          fetch(`${BACKEND_API_URL}/animal/getAll`)
          .then((response) => response.json())
          .then((count) => {
            fetch(`${BACKEND_API_URL}/animal/getAll?pageNo=${currentPage}&pageSize=${pageSize}`)
            .then((response) => response.json())
            .then((data) => {
              setTotal(count);
              setAnimals(data);
              setLoading(false);
            });
          })
          .catch((error) => {
            console.error(error);
            setLoading(false);
          });
        };
        fetchAnimals();
      }, [currentPage, pageSize]);


    // useEffect(() => {
    //     fetch(`${BACKEND_API_URL}/animal/getAll`) // ?pageNo=${page}&pageSize=${pageSize}
    //         .then(res => res.json())
    //         .then(data => {setAnimals(data); setLoading(false);})
    // }, []);

    // console.log(animals);

    const[weight, setWeight] = useState(0);

    

    return (

        <Container>
            <h1 style={{marginTop:"65px"}}>All Animals</h1>

            {loading && <CircularProgress />}

            {!loading && animals.length == 0 && <div>No animals found</div>}

            {!loading && (
            <div style ={{display: "flex", alignItems:"center"}}>
               
                <Button
                  sx={{color:"red"}}
                  disabled={currentPage===0}
                  onClick={handlePreviousPage}>
                    Previous Page
                </Button>
                <Button
                 sx={{color:"red"}} onClick={handleNextPage}>
                  Next Page
                 </Button>

                 <Box mx={2} display="flex" alignItems="center">
                  Page {currentPage+1} of {Math.ceil(total/pageSize)}
                 </Box>
            </div>
            )}

            {!loading && animals.length > 0 && (
            <>
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
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Operations
                                    <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/add`}>
                                        <Tooltip title="Add a new animal" arrow>
                                            <AddIcon style={{color:"black", fontSize:"20px"}} />
                                        </Tooltip>
                                    </IconButton>
                                    <Box sx={{display: 'inline-flex'}}>
                                        <IconButton 
                                        component={Link} 
                                        sx={{ mr: 3 }} 
                                        to={`/animal/filter/${weight}`}
                                        onClick={() => setWeight(0)}
                                        >
                                            <Tooltip title="Get animals with weight higher than a given weight." arrow>
                                            <FilterAltIcon style={{color:"black", fontSize:"20px"}} />
                                            </Tooltip>
                                        </IconButton>
                                        <TextField 
                                        label="Enter weight" 
                                        variant="outlined" 
                                        size="small" 
                                        value={weight}
                                        onChange={(event) => setWeight(Number(event.target.value))}/>
                                    </Box>
                                </TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {animals.map((animal:Animal, index) => (
                                <TableRow key={animal.animalId}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{animal.name}</TableCell>
                                    <TableCell align="center">{animal.type}</TableCell>
                                    <TableCell align="center">{animal.weight}</TableCell>
                                    <TableCell align="center">{animal.dateOfBirth}</TableCell>
                                    <TableCell align="center">{animal.breed}</TableCell> 
                                    <TableCell align="center">
                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/${animal.animalId}`}>
                                            <VisibilityIcon  style={{color:"black", fontSize:"20px"}}/>
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/update/${animal.animalId}`}>
                                            <EditIcon sx={{ color: "navy" }}/>
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/delete/${animal.animalId}`}>
                                            <DeleteIcon sx={{ color: "darkred" }} />
                                        </IconButton>

                                        
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <Button
          sx={{color:"red"}}
          disabled={currentPage===0}
          onClick={handlePreviousPage}>
            Previous Page
          </Button>

        <Button sx={{color:"red"}} onClick={handleNextPage}>
          Next Page
        </Button>
                {/* <Paginator
                        rowsPerPage={pageSize}
                        totalRows={totalRows}
                        currentPage={page}
                        isFirstPage={page === 1}
                        isLastPage={isLastPage}
                        setPage={setCurrentPage}
                        goToNextPage={goToNextPage}
                        goToPrevPage={goToPrevPage}
                    /> */}
            </>
            )
            }
        </Container>

    );
}