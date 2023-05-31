using api.Dtos.User;
using api.Responses;

namespace api.Services
{
    public interface IAuthService
    {
        Task<DetailedUserDto> GetUserAsync(Guid id);
        Task<UserDto> RegisterAsync(RegisterUserDto user);
        LoginResponse<UserDto> Login(LoginUserDto user);
    }
}