using api.Dtos.PublicDestinations;
using api.Services;
using Microsoft.AspNetCore.Mvc;
using api.Exceptions;
using Microsoft.AspNetCore.Authorization;
using api.Dtos.PrivateDestination;

namespace api.Controllers
{

    [ApiController]
    [Authorize]
    [Route("api/[controller]")]
    public class PrivateDestinationsController : ControllerBase
    {
        public PrivateDestinationsService service;

        public PrivateDestinationsController(IPrivateDestinationsService service)
        {
            this.service = (PrivateDestinationsService) service;
        }

        // GET /privatedestinations
        [HttpGet]
        [AllowAnonymous]
        //[Authorize(Roles = "Admin")]
        public async Task<ActionResult<IEnumerable<PublicDestinationDto>>> GetPrivateDestinationsAsync()
        {
            try
            {
                var publicDestinations = await this.service.GetAllAsync();
                return Ok(publicDestinations);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ForbiddenException e)
            {
                return BadRequest(e.Message);
            }
        }
        
        // GET /privatedestinations/:id
        [HttpGet("{id}")]
        [Authorize(Roles = "Admin,Normal")]
        public async Task<ActionResult<IEnumerable<PublicDestinationDto>>> GetPrivateDestinationAsync(Guid id)
        {
            try
            {
                var privateDestination = await this.service.GetByIdAsync(id);
                return Ok(privateDestination);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ForbiddenException e)
            {
                return BadRequest(e.Message);
            }
        }
        
        // ADD /privatedestinations
        [HttpPost]
        [Authorize(Roles = "Admin,Normal")]
        public async Task<ActionResult<PublicDestinationDto>> AddPrivateDestinationAsync(AddPrivateDestinationDto privateDestination)
        {
            try
            {
                var newPrivateDestinations = await this.service.AddAsync(privateDestination);
                return Ok(newPrivateDestinations);
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ForbiddenException e)
            {
                return BadRequest(e.Message);
            }
        }
        
        // PUT /privatedestinations/:id
        [HttpPut("{id}")]
        [Authorize(Roles = "Admin,Normal")]
        public async Task<ActionResult> UpdatePrivateDestinationAsync(Guid id, UpdatePrivateDestinationDto privateDestination)
        {
            try
            {
                await this.service.UpdateAsync(id, privateDestination);
                return NoContent();
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ForbiddenException e)
            {
                return BadRequest(e.Message);
            }
        }

        // DELETE /privatedestination/:id
        [HttpDelete("{id}")]
        [Authorize(Roles = "Admin,Normal")]
        public async Task<ActionResult> DeletePrivateDestiantion(Guid id)
        {
            try
            {
                await this.service.DeleteAsync(id);
                return NoContent();
            }
            catch (NotFoundException e)
            {
                return NotFound(e.Message);
            }
            catch (ForbiddenException e)
            {
                return BadRequest(e.Message);
            }
        }
    }
}