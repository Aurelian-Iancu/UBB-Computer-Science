using api.Dtos.PublicDestinations;
using Microsoft.EntityFrameworkCore;
using api.Exceptions;
using api.Repositories;
using api.Models;
using api.Validators;

namespace api.Services
{
    public class PublicDestinationsService : IPublicDestinationsService
    {
        private readonly DatabaseContext context;
        private readonly PublicDestinationValidator validator;

        public PublicDestinationsService(DatabaseContext context, PublicDestinationValidator validator)
        {
            this.context = context;
            this.validator = validator;
        }

        public async Task<IEnumerable<PublicDestinationDto>> GetAllAsync()
        {
            var publicDestinations = await this.context.PublicDestinations.ToListAsync();

            if (publicDestinations is null)
            {
                throw new NotFoundException("Destinations not found.");
            }

            return publicDestinations.Select(destination => destination.AsDto());
        }

        public async Task<PublicDestinationDto> GetByIdAsync(Guid id)
        {
            var publicDestination = await this.context.PublicDestinations.FindAsync(id);

            if (publicDestination is null)
            {
                throw new NotFoundException("Destination not found.");
            }

            return publicDestination.AsDto();
        }

        public async Task<PublicDestinationDto> AddAsync(AddPublicDestinationDto publicDestination)
        {
            var newPublicDestination = new Destination 
            {
                Id = Guid.NewGuid(),
                Geolocation = publicDestination.Geolocation,
                Title = publicDestination.Title,
                Image = publicDestination.Image,
                Description = publicDestination.Description
            };

            var result = this.validator.ValidatePublicDestination(newPublicDestination);
            if (result != string.Empty)
            {
                throw new ValidationException(result);
            }

            await this.context.PublicDestinations.AddAsync(newPublicDestination);
            await this.context.SaveChangesAsync();

            return newPublicDestination.AsDto();
        }

        public async Task UpdateAsync(Guid id, UpdatePublicDestinationDto publicDestination)
        {
            var oldPublicDestination = await this.context.PublicDestinations.FindAsync(id);
            
            if (oldPublicDestination is null)
            {
                throw new NotFoundException("Destination not found.");
            }
            
            var result = this.validator.ValidatePublicDestinationDto(publicDestination);
            if (result != string.Empty)
            {
                throw new ValidationException(result);
            }

            oldPublicDestination.Geolocation = publicDestination.Geolocation == string.Empty ?
                oldPublicDestination.Geolocation : publicDestination.Geolocation;
            oldPublicDestination.Title = publicDestination.Title == string.Empty ?
                oldPublicDestination.Title : publicDestination.Title;
            oldPublicDestination.Image = publicDestination.Image == string.Empty ?
                oldPublicDestination.Image : publicDestination.Image;
            oldPublicDestination.Description = publicDestination.Description == string.Empty ?
                oldPublicDestination.Description : publicDestination.Description;

            await this.context.SaveChangesAsync();
        }

        public async Task DeleteAsync(Guid id)
        {
            var publicDestination = await this.context.PublicDestinations.FindAsync(id);

            if (publicDestination is null) 
            {
                throw new NotFoundException("Destination not found.");
            }

            this.context.Remove(publicDestination);
            await this.context.SaveChangesAsync();
        }
    }
}