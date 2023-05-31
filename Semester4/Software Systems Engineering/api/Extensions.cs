using api.Dtos.PrivateDestination;
using api.Dtos.PublicDestinations;
using api.Dtos.User;
using api.Models;

namespace api
{
    public static class Extension
    {
        public static PublicDestinationDto AsDto(this Destination destination)
        {
            return new PublicDestinationDto
            {
                Id = destination.Id,
                Geolocation = destination.Geolocation,
                Title = destination.Title,
                Image = destination.Image,
                Description = destination.Description
            };
        }

        public static PrivateDestinationDto AsDto(this PrivateDestination destination)
        {
            return new PrivateDestinationDto
            {
                Id = destination.Id,
                Geolocation = destination.Geolocation,
                Title = destination.Title,
                Image = destination.Image,
                Description = destination.Description,
                StartDate = destination.StartDate,
                EndDate = destination.EndDate,
                UserId = destination.UserId
            };
        }
        
        public static UserDto AsDto(this User user)
        {
            return new UserDto
            {
                Id = user.Id,
                Username = user.Username,
                Roles = user.Roles
            };
        }
        
        public static DetailedUserDto AsDetailedDto(this User user)
        {
            return new DetailedUserDto
            {
                Id = user.Id,
                Username = user.Username,
                Roles = user.Roles,
                BucketList = user.Destinations is not null 
                    ? user.Destinations.Select(d => d.AsDto()).ToList() 
                    : new List<PrivateDestinationDto>()
            };
        }
    }
}