namespace api.Dtos.PublicDestinations
{
    public record UpdatePublicDestinationDto
    {
        public string Geolocation { get; set; } = string.Empty;
        public string Title { get; set; } = string.Empty;
        public string Image { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
    }
}