resource "aws_internet_gateway" "bigbro-gw" {
  vpc_id = aws_vpc.bigbro-vpc.id

  tags = {
    Name    = "bigbro-gw"
    Project = var.project_name
  }
}