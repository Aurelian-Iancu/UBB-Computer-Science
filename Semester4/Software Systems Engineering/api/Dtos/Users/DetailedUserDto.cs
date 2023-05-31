using api.Dtos.PrivateDestination;

namespace api.Dtos.User
{
    public record DetailedUserDto
    {
        public Guid Id { get; set; }
        public string Username { get; set; } = string.Empty;
        public string Roles { get; set; } = string.Empty;
        public ICollection<PrivateDestinationDto> BucketList { get; set; } = new List<PrivateDestinationDto>();
    }
}