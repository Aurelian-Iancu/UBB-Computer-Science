import { Button, Container } from "@mui/material";
import { Link } from 'react-router-dom';

export const Statistics = () => {
  return (
    <>
    <Container sx={{ display: 'flex', flexDirection: 'row' }}>
      <Button style={{color:"whitesmoke", border: '1px solid whitesmoke'}} component={Link} sx={{ mr: 3 }} to="/shelter/statistics/countAnimal">
        Shelters ordered by number of animals.
      </Button>

   
      <Button style={{color:"whitesmoke", border: '1px solid whitesmoke'}} component={Link} sx={{ mr: 3 }} to="/shelter/statistics/averageWeight">
       Shelters ordered by average weight of the animals.
      </Button>
    
    </Container>
    </>
  );
};