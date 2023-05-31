using Microsoft.AspNetCore.Mvc;
using api.Exceptions;
using api.Responses;
using api.Services;
using api.Dtos.User;

namespace api.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly AuthService service;

        public AuthController(IAuthService service) 
        {
            this.service = (AuthService) service;
        }

        // GET /auth/user
        [HttpGet("user/{id}")]
        public async Task<ActionResult<DetailedUserDto>> GetUserAsync(Guid id) 
        {
            try
            {
                var detailedUserDto = await this.service.GetUserAsync(id);
                return Ok(detailedUserDto);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
        }

        // POST /auth/register
        [HttpPost("register")]
        public async Task<ActionResult<string>> RegisterAsync(RegisterUserDto user) 
        {
            try
            {
                var userDto = await this.service.RegisterAsync(user);
                return Ok(userDto);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ValidationException e)
            {
                return ValidationProblem(e.Message);
            }
        }
        
        // POST /auth/login
        [HttpPost("login")]
        public ActionResult<LoginResponse<UserDto>> LoginAsync(LoginUserDto user) 
        {
            try
            {
                var loginResponse = this.service.Login(user);
                return Ok(loginResponse);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ValidationException e)
            {
                return ValidationProblem(e.Message);
            }
        }
    }
}