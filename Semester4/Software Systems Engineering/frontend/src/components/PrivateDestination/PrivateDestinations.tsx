import React, { useEffect, useState } from 'react';
import { Table, Button } from 'antd';
import { Destination } from '../../../../../../../../Downloads/frontend/src/Destination';
import {useNavigate} from "react-router-dom";
  
  export const PrivateDestinations = () => {
    const navigate = useNavigate();
    const[destinations, setDestinations] = useState([]);

    const user = localStorage.getItem('item');
    const item = JSON.parse(user);
    const userId = item ? item.userid : null;
    const token = item ? item.token : null;

      useEffect(() => {
          const fetchDestinations = async () => {
              try {
                  const response = await fetch(`https://localhost:7203/api/Auth/user/${userId}`, {
                      headers: {
                          Authorization: `Bearer ${token}`,
                      },
                  });
                  const data = await response.json();
                  setDestinations(data.bucketList);
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
              title: 'StartDate',
              dataIndex: 'startDate',
              key: 'startDate',
          },
          {
              title: 'EndDate',
              dataIndex: 'endDate',
              key: 'endDate',
          },
          {
              title: 'Actions',
              key: 'actions',
              render: (text: any, destination: Destination) => (
                  <div>
                      <Button
                          type="primary"
                          onClick={() => handleDeleteDestination(destination.id)}
                          style={{ marginLeft: '8px' }}
                      >
                          Delete
                      </Button>
                  </div>
              ),
          },
      ];


      const handleDeleteDestination = async (destinationId: number) => {
          try {
              const response = await fetch(`https://localhost:7203/api/PrivateDestinations/${destinationId}`, {
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

      const handleAddPrivateDestination = () => {
          navigate('/addprivatedestination');
      };

      return (
          <div>
              <h1 style={{ fontSize: '24px', marginTop: '0px' }}>All Destinations</h1>
              <div style={{ width: '80%', margin: 'auto' }}>
                  <Table dataSource={destinations} columns={columns} rowKey="id" />
              </div>
              <Button type="primary" onClick={handleAddPrivateDestination} style={{ marginTop: '16px' }}>
                  Add Private Destination
              </Button>
          </div>
      );
  };
  
  export default PrivateDestinations;