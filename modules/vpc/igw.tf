resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.bigbro.id

  tags = {
    Name    = "gw"
    Project = var.project_name
  }
}