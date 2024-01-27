using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace StopCorruption.Data.Migrations
{
    /// <inheritdoc />
    public partial class Seconddmigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Application_Sector_SectorId",
                table: "Application");

            migrationBuilder.DropForeignKey(
                name: "FK_Application_User_UserId",
                table: "Application");

            migrationBuilder.AddForeignKey(
                name: "FK_Application_Sector_SectorId",
                table: "Application",
                column: "SectorId",
                principalTable: "Sector",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Application_User_UserId",
                table: "Application",
                column: "UserId",
                principalTable: "User",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Application_Sector_SectorId",
                table: "Application");

            migrationBuilder.DropForeignKey(
                name: "FK_Application_User_UserId",
                table: "Application");

            migrationBuilder.AddForeignKey(
                name: "FK_Application_Sector_SectorId",
                table: "Application",
                column: "SectorId",
                principalTable: "Sector",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);

            migrationBuilder.AddForeignKey(
                name: "FK_Application_User_UserId",
                table: "Application",
                column: "UserId",
                principalTable: "User",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
