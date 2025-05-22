resource "aws_vpc" "bigbro" {
  cidr_block  = var.vpc_cidr

  tags = {
    Name      = "bigbro"
    Project   = var.project_name
  }
}