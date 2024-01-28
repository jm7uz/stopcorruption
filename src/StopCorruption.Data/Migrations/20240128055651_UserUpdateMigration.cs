using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace StopCorruption.Data.Migrations
{
    /// <inheritdoc />
    public partial class UserUpdateMigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "OneID",
                table: "User",
                newName: "passportNumber");

            migrationBuilder.AddColumn<string>(
                name: "FullName",
                table: "User",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "Language",
                table: "User",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "PermitAddress",
                table: "User",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "Phone",
                table: "User",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "passportIssuedBy",
                table: "User",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<int>(
                name: "PeriodType",
                table: "Application",
                type: "integer",
                nullable: false,
                defaultValue: 0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "FullName",
                table: "User");

            migrationBuilder.DropColumn(
                name: "Language",
                table: "User");

            migrationBuilder.DropColumn(
                name: "PermitAddress",
                table: "User");

            migrationBuilder.DropColumn(
                name: "Phone",
                table: "User");

            migrationBuilder.DropColumn(
                name: "passportIssuedBy",
                table: "User");

            migrationBuilder.DropColumn(
                name: "PeriodType",
                table: "Application");

            migrationBuilder.RenameColumn(
                name: "passportNumber",
                table: "User",
                newName: "OneID");
        }
    }
}
