using AutoMapper;
using StopCorruption.Domain.Entities;
using StopCorruption.Service.DTOs.Applications;
using StopCorruption.Service.DTOs.ChatMessages;
using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.DTOs.Users;

namespace StopCorruption.Service.Mappers
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<User, UserForCreationDto>().ReverseMap();
            CreateMap<User, UserForUpdateDto>().ReverseMap();
            CreateMap<User, UserForResultDto>().ReverseMap();

            CreateMap<Sector, SectorForCreationDto>().ReverseMap();
            CreateMap<Sector, SectorForUpdateDto>().ReverseMap();
            CreateMap<Sector, SectorForResultDto>().ReverseMap();

            CreateMap<Application, ApplicationForCreationDto>().ReverseMap();
            CreateMap<Application, ApplicationForUpdateDto>().ReverseMap();
            CreateMap<Application, ApplicationForResultDto>().ReverseMap();

            CreateMap<ChatMessage, ChatMessageForCreationDto>().ReverseMap();
            CreateMap<ChatMessage, ChatMessageForUpdateDto>().ReverseMap();
            CreateMap<ChatMessage, ChatMessageForResultDto>().ReverseMap();

        }
    }
}
