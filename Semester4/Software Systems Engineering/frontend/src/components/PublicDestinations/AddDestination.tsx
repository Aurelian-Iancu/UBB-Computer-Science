import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const AddDestination = () => {
  const [geolocation, setGeolocation] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const user = localStorage.getItem('item');
  const item = JSON.parse(user);
  const userRole = item ? item.roles : null;
  const token = item ? item.token : null;

  const navigate = useNavigate();

  const handleGeolocationChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setGeolocation(event.target.value);
  };

  const handleTitleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setTitle(event.target.value);
  };

  const handleDescriptionChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setDescription(event.target.value);
  };

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setImage(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
  
    try {
      const response = await fetch('https://localhost:7203/api/PublicDestinations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          geolocation,
          title,
          description,
          image,
        }),
      });
  
      if (response.ok) {
        // Destination added successfully
        setGeolocation('');
        setTitle('');
        setDescription('');
        setImage('');
        console.log('Destination added successfully');
        navigate('/alldestinations'); // Redirect to the desired page

      } else {
        // Error occurred while adding destination
        console.error('Error adding destination');
      }
    } catch (error) {
      console.error('Error adding destination:', error);
    }
  };
  

  return (
    <div>
      <h1>Add Destination</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="geolocation">Geolocation:</label>
          <input type="text" id="geolocation" value={geolocation} onChange={handleGeolocationChange} required />
        </div>
        <div>
          <label htmlFor="title">Title:</label>
          <input type="text" id="title" value={title} onChange={handleTitleChange} required />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <input type="text" id="description" value={description} onChange={handleDescriptionChange} required />
        </div>
        <div>
          <label htmlFor="image">Image:</label>
          <input type="text" id="image" value={image} onChange={handleImageChange} required />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddDestination;
