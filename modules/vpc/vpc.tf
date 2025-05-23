resource "aws_vpc" "bigbro-vpc" {
  cidr_block = var.vpc_cidr

  tags = {
    Name    = "bigbro-vpc"
    Project = var.project_name
  }
}