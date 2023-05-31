import { Box, AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";
import HomeIcon from '@mui/icons-material/Home';
import AirplanemodeActiveIcon from '@mui/icons-material/AirplanemodeActive';


export function AppMenu(){
	const user = localStorage.getItem('item');
	const item = JSON.parse(user);
	const userName = item ? item.username : null;
	const userRole = item ? item.roles : null;

	const handleLogout = () => {
		localStorage.removeItem('item');
		window.location.href = '/login';
	};

	return (
		<Box>
			<AppBar style={{backgroundColor:"#34495E"}}>
				<Toolbar>


					{userName ? (
						<>
							<Typography variant="h6" component="div" sx={{ mr: 5 }}>
								Destination bucket list
							</Typography>


							{userRole === "Admin" ? (
								<>
									<Button
										to="/alldestinations"
										component={Link}
										color="inherit"
										sx={{ mr: 5 }}
										startIcon={<AirplanemodeActiveIcon />}>
										All destinations
									</Button>
								</>
							) : (<>
									<Button
										to="/pickpublic"
										component={Link}
										color="inherit"
										sx={{ mr: 5 }}
										startIcon={<AirplanemodeActiveIcon />}>
										All available destinations
									</Button>

									<Button
										to="/privatedestinations"
										component={Link}
										color="inherit"
										sx={{ mr: 5 }}
										startIcon={<AirplanemodeActiveIcon />}>
										Private destinations
									</Button>

							</>)}


							<Button color="inherit" sx={{ mr: 5 }} onClick={handleLogout}>
								Logout
							</Button>
							<Typography variant="h6" component="div" sx={{ mr: 5 }}>
								User: {userName}
							</Typography>
						</>
					) : (
						<>
							<IconButton
								component={Link}
								to="/"
								size="large"
								edge="start"
								color="inherit"
								aria-label="school"
								sx={{ mr: 2 }}>
								<HomeIcon />
							</IconButton></>
					)}
				</Toolbar>
			</AppBar>
		</Box>
	);
}