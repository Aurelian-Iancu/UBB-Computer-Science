import React, { useEffect, useState } from 'react';
import { Table, Button } from 'antd';
import { useNavigate } from 'react-router-dom';
import { Destination } from '../../Destination';

export const AllDestinations = () => {
  const [destinations, setDestinations] = useState<Destination[]>([]);
  const navigate = useNavigate();
  const user = localStorage.getItem('item');
  const item = JSON.parse(user);
  const userId = item ? item.userid : null;
  const token = item ? item.token : null;

  useEffect(() => {
    const fetchDestinations = async () => {
      try {
        const response = await fetch('https://localhost:7203/api/PublicDestinations', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const data = await response.json();
        setDestinations(data);
      } catch (error) {
        console.error('Error fetching destinations:', error);
      }
    };
    fetchDestinations();
  }, []);

  const columns = [
    {
      title: 'Title',
      dataIndex: 'title',
      key: 'title',
    },
    {
      title: 'Image',
      dataIndex: 'image',
      key: 'image',
      render: (image: string) => <img src={image} alt="Destination" height={50} />,
    },
    {
      title: 'Description',
      dataIndex: 'description',
      key: 'description',
    },
    {
      title: 'Geolocation',
      dataIndex: 'geolocation',
      key: 'geolocation',
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (text: any, destination: Destination) => (
          <div>
            <Button
                type="primary"
                onClick={() => handleUpdateDestination(destination)}
                style={{ marginRight: '8px' }}
            >
              Update
            </Button>
            <Button type="primary" onClick={() => handleDeleteDestination(destination.id)}>
              Delete
            </Button>
          </div>
      ),
    }
    // Add more columns as needed
  ];

  const handleAddDestination = () => {
    navigate('/adddestination');
  };

  const handleUpdateDestination = (destination: Destination) => {
    navigate('/updateDestination', { state: { destination } });
  };

  const handleDeleteDestination = async (destinationId: number) => {
    try {
      const response = await fetch(`https://localhost:7203/api/PublicDestinations/${destinationId}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`,
        }
      });

      if (response.ok) {
        console.log('Destination deleted successfully');
        // Perform any necessary actions after successfully deleting the destination
        // Fetch the updated list of destinations or update the state accordingly
        const updatedDestinations = destinations.filter(destination => destination.id !== destinationId);
        setDestinations(updatedDestinations);
      } else {
        console.error('Error deleting destination');
      }
    } catch (error) {
      console.error('Error deleting destination:', error);
    }
  };


  return (
      <div>
        <h1 style={{ fontSize: '24px', marginTop: '0px' }}>All Destinations</h1>
        <div style={{ width: '80%', margin: 'auto' }}>
          <Table dataSource={destinations} columns={columns} rowKey="id" />
        </div>
        <Button type="primary" onClick={handleAddDestination} style={{ marginTop: '20px' }}>
          Add Destination
        </Button>
      </div>
  );
};

export default AllDestinations;