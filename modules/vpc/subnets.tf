resource "aws_subnet" "public_subnet_1" {
  vpc_id            = aws_vpc.bigbro-vpc.id
  cidr_block        = var.public_subnet_1_cidr
  availability_zone = "ap-northeast-2a"

  tags = {
    Name    = "public_subnet_1"
    Project = var.project_name
  }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id            = aws_vpc.bigbro-vpc.id
  cidr_block        = var.public_subnet_2_cidr
  availability_zone = "ap-northeast-2b"

  tags = {
    Name    = "public_subnet_2"
    Project = var.project_name
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id     = aws_vpc.bigbro-vpc.id
  cidr_block = var.private_subnet_1_cidr

  tags = {
    Name    = "private_subnet_1"
    Project = var.project_name
  }
}