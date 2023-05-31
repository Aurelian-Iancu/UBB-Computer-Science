using api.Dtos.PrivateDestination;

namespace api.Services
{
    public interface IPrivateDestinationsService
    {
        Task<IEnumerable<PrivateDestinationDto>> GetAllAsync();
        Task<PrivateDestinationDto> GetByIdAsync(Guid id);
        Task<PrivateDestinationDto> AddAsync(AddPrivateDestinationDto privateDestination);
        Task UpdateAsync(Guid id, UpdatePrivateDestinationDto privateDestination);
        Task DeleteAsync(Guid id);
    }
}