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
    Box,
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
import SortIcon from '@mui/icons-material/Sort';

export const SheltersShowAll = () => {
    const[loading, setLoading] = useState(true);
    const[shelters, setShelters] = useState([]);
    const [pageSize, setPageSize] = useState(100);
    const [total, setTotal] =useState(0)
    const [currentPage, setCurrentPage]=useState(0)

    // useEffect(() => {
    //     fetch(`${BACKEND_API_URL}/shelter/getAll`)
    //         .then(res => res.json())
    //         .then(data => {setShelters(data); setLoading(false);})
    // }, []);

    useEffect(() => {
        setLoading(true);
    
        const fetchShelters = () => {
          fetch(`${BACKEND_API_URL}/shelter/getAll`)
          .then((response) => response.json())
          .then((count) => {
            fetch(`${BACKEND_API_URL}/shelter/getAll?pageNo=${currentPage}&pageSize=${pageSize}`)
            .then((response) => response.json())
            .then((data) => {
              setTotal(count);
              setShelters(data);
              setLoading(false);
            });
          })
          .catch((error) => {
            console.error(error);
            setLoading(false);
          });
        };
        fetchShelters();
      }, [currentPage, pageSize]);

      const handlePreviousPage = () => {
        if(currentPage>0)
        {
          setCurrentPage(currentPage-1);
        }
      };
    
      const handleNextPage = () => {
        setCurrentPage(currentPage+1);
      };

    console.log(shelters);

    const sortShelters = () => {
        const sortedShelters = [...shelters].sort((a: Shelter, b: Shelter) => {
            if (a.capacity < b.capacity) {
                return -1;
            }
            if (a.capacity > b.capacity) {
                return 1;
            }
            return 0;
        })
        console.log(sortedShelters);
        setShelters(sortedShelters);
    }

    return (
        <>
        <Container>
            <h1 style={{marginTop:"65px"}}>All Shelters</h1>

            {loading && <CircularProgress />}

            {!loading && shelters.length == 0 && <div>No shelters found</div>}

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

            {!loading && shelters.length > 0 && (

                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 800 }} aria-label="simple table" style={{backgroundColor:"whitesmoke"}}>
                        <TableHead>
                            <TableRow>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Crt.</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight:'bold'}}>Name</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Address</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Number of volunteers</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Description</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>
                                    Capacity
                                <IconButton sx={{color:"black", paddingLeft:2, fontSize:"20px", width:"20px", '&:focus': {
                                            outline: "none"
                                        } }} onClick={sortShelters}>
                                        <Tooltip title="Sort" arrow>
                                            <SortIcon style={{color:"black", fontSize:"20px"}} />
                                        </Tooltip>
                                    </IconButton></TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>City</TableCell>
                                <TableCell align="center" style={{color:"#2471A3", fontWeight: 'bold'}}>Operations
                                    <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/save`}>
                                        <Tooltip title="Add a new shelter" arrow>
                                            <AddIcon style={{color:"black", fontSize:"20px"}} />
                                        </Tooltip>
                                    </IconButton>
                                    <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/statistics-countAnimal`}>
                                        <Tooltip title="Get shelters ordered by number of animals." arrow>
                                            <FilterAltIcon style={{color:"black", fontSize:"20px"}} />
                                        </Tooltip>
                                    </IconButton></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {shelters.map((shelter:Shelter, index) => (
                                <TableRow key={shelter.shelterId}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{shelter.name}</TableCell>
                                    <TableCell align="center">{shelter.address}</TableCell>
                                    <TableCell align="center">{shelter.numberOfVolunteers}</TableCell>
                                    <TableCell align="center">{shelter.description}</TableCell>
                                    <TableCell align="center">{shelter.capacity}</TableCell>
                                    <TableCell align="center">{shelter.city}</TableCell> 
                                    <TableCell align="center">
                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/${shelter.shelterId}`}>
                                            <VisibilityIcon  style={{color:"black", fontSize:"20px"}}/>
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/update/${shelter.shelterId}`}>
                                            <EditIcon sx={{ color: "navy" }}/>
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/delete/${shelter.shelterId}`}>
                                            <DeleteIcon sx={{ color: "darkred" }} />
                                        </IconButton>
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                
            )
            
            }
            <Button
          sx={{color:"red"}}
          disabled={currentPage===0}
          onClick={handlePreviousPage}>
            Previous Page
          </Button>

        <Button sx={{color:"red"}} onClick={handleNextPage}>
          Next Page
        </Button>
        </Container>
        </>
    );
}