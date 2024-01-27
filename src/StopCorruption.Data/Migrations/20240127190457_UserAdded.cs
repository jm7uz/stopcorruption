using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace StopCorruption.Data.Migrations
{
    /// <inheritdoc />
    public partial class UserAdded : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Period",
                table: "Statistics");

            migrationBuilder.AddColumn<string>(
                name: "District",
                table: "Statistics",
                type: "text",
                nullable: true);

            migrationBuilder.AddColumn<int>(
                name: "PeriodType",
                table: "Statistics",
                type: "integer",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "Region",
                table: "Statistics",
                type: "integer",
                nullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "MediaPath",
                table: "Application",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "District",
                table: "Statistics");

            migrationBuilder.DropColumn(
                name: "PeriodType",
                table: "Statistics");

            migrationBuilder.DropColumn(
                name: "Region",
                table: "Statistics");

            migrationBuilder.AddColumn<string>(
                name: "Period",
                table: "Statistics",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AlterColumn<string>(
                name: "MediaPath",
                table: "Application",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);
        }
    }
}
