﻿using StopCorruption.Domain.Commons;

namespace StopCorruption.Domain.Entities;

public class Sector : Auditable
{
    public string SectorName { get; set; }
}