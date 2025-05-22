resource "aws_subnet" "public_subnet_1" {
  vpc_id     = aws_vpc.bigbro.id
  cidr_block = var.public_subnet_1_cidr

  tags = {
    Name    = "public_subnet_1"
    Project = var.project_name
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id     = aws_vpc.bigbro.id
  cidr_block = var.private_subnet_1_cidr

  tags = {
    Name    = "private_subnet_1"
    Project = var.project_name
  }
}