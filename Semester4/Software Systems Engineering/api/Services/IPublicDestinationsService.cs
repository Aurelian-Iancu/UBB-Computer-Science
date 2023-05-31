using api.Dtos.PublicDestinations;

namespace api.Services
{
    public interface IPublicDestinationsService
    {
        Task<IEnumerable<PublicDestinationDto>> GetAllAsync();
        Task<PublicDestinationDto> GetByIdAsync(Guid id);
        Task<PublicDestinationDto> AddAsync(AddPublicDestinationDto publicDestination);
        Task UpdateAsync(Guid id, UpdatePublicDestinationDto publicDestination);
        Task DeleteAsync(Guid id);
    }
}